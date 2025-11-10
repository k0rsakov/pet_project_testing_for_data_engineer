import pendulum
import requests

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator


OWNER = "i.korsakov"
DAG_ID = "bad_etl_pattern_for_testing_users_to_pg"
SHORT_DESCRIPTION = "Антипаттерн: все этапы ETL в одной функции"
LONG_DESCRIPTION = """
# LONG DESCRIPTION
"""

PG_CONN_ID = "dwh"
PG_SCHEMA = "public"
PG_TABLE = "users"

args = {
    "owner": OWNER,
    # "start_date": pendulum.datetime(year=20240, month=1, day=1, tz="Europe/Moscow"),
    "start_date": pendulum.datetime(year=2024, month=1, day=1, tz="Europe/Moscow"),
    "catchup": False,
    "retries": 1,
    "retry_delay": pendulum.duration(minutes=15),
    "depends_on_past": False,
}


def etl_load_user_to_pg():
    # 1. Получаем данные по API
    response = requests.get("https://randomuser.me/api/")
    if response.status_code != 200:
        raise Exception(f"Ошибка получения данных: {response.status_code}")
    user_data = response.json()

    # 2. Забираем поля
    user = user_data["results"][0]
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    email = user["email"]
    city = user["location"]["city"]
    country = user["location"]["country"]

    # 3. Подключаемся к БД и пишем данные
    pg_hook = PostgresHook(postgres_conn_id=PG_CONN_ID)
    insert_sql = f"""
        INSERT INTO {PG_SCHEMA}.{PG_TABLE} 
            (first_name, last_name, email, city, country)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(city)s, %(country)s);
    """
    pg_hook.run(
        sql=insert_sql,
        parameters={"first_name": first_name, "last_name": last_name, "email": email, "city": city, "country": country},
    )


with DAG(
    dag_id=DAG_ID,
    schedule_interval="0 10 * * *",
    default_args=args,
    tags=["etl", "bad_example", "postgres"],
    catchup=False,
    description=SHORT_DESCRIPTION,
    concurrency=1,
    max_active_tasks=1,
    max_active_runs=1,
) as dag:
    dag.doc_md = LONG_DESCRIPTION

    start = EmptyOperator(task_id="start")

    etl_task = PythonOperator(
        task_id="etl_load_user_to_pg",
        python_callable=etl_load_user_to_pg,
    )

    end = EmptyOperator(task_id="end")

    start >> etl_task >> end
