import pendulum

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

from extensions_for_orchestration.extensions_api import get_api_response
from extensions_for_orchestration.extensions_transform import extract_user_fields
from extensions_for_orchestration.extensions_postgresql import save_user_to_pg

OWNER = "i.korsakov"
DAG_ID = "good_etl_pattern_for_testing_users_to_pg"
SHORT_DESCRIPTION = "Хороший паттерн: декомпозиция ETL"
LONG_DESCRIPTION = """
# LONG DESCRIPTION

Декомпозированный DAG загрузки пользователей из randomuser.me в Postgres.
"""

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


def etl_user_to_pg_task():
    """
    Задача загрузки произвольного пользователя из randomuser.me в PostgreSQL.
    """
    api_data = get_api_response()
    user = extract_user_fields(api_data)
    save_user_to_pg(user, PG_CONN_ID, PG_SCHEMA, PG_TABLE)


with DAG(
    dag_id=DAG_ID,
    schedule_interval="0 10 * * *",
    default_args=args,
    tags=["etl", "good_example", "postgres"],
    catchup=False,
    description=SHORT_DESCRIPTION,
    concurrency=1,
    max_active_tasks=1,
    max_active_runs=1,
) as dag:
    dag.doc_md = LONG_DESCRIPTION

    start = EmptyOperator(task_id="start")
    etl_task = PythonOperator(
        task_id="etl_user_to_pg_task",
        python_callable=etl_user_to_pg_task,
    )
    end = EmptyOperator(task_id="end")

    start >> etl_task >> end
