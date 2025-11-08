from typing import Dict
from airflow.providers.postgres.hooks.postgres import PostgresHook


def save_user_to_pg(user: Dict[str, str], conn_id: str, schema: str, table: str) -> None:
    """
    Сохраняет пользователя в PostgreSQL через PostgresHook.

    :param user: Словарь с user-полями
    :param conn_id: Имя соединения в Airflow (например, 'dwh')
    :param schema: Схема БД в Postgres
    :param table: Имя таблицы
    """
    pg_hook = PostgresHook(postgres_conn_id=conn_id)
    insert_sql = f"""
        INSERT INTO {schema}.{table} (first_name, last_name, email, city, country)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(city)s, %(country)s);
    """
    pg_hook.run(
        sql=insert_sql,
        parameters=user,
    )
