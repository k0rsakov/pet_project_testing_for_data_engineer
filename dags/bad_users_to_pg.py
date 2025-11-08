import pendulum
import requests
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook

OWNER = "i.korsakov"
DAG_ID = "bad_users_to_pg"

PG_CONN_ID = "dwh"
PG_SCHEMA = "public"
PG_TABLE = "users"

args = {
    "owner": OWNER,
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
        INSERT INTO {PG_SCHEMA}.{PG_TABLE} (first_name, last_name, email, city, country)
        VALUES (%s, %s, %s, %s, %s)
    """
    pg_hook.run(insert_sql, parameters=(first_name, last_name, email, city, country))

with DAG(
    dag_id=DAG_ID,
    schedule=None,
    default_args=args,
    tags=["etl", "bad_example", "postgres"],
    description="Антипаттерн: все этапы ETL в одной функции",
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id="etl_load_user_to_pg",
        python_callable=etl_load_user_to_pg,
    )