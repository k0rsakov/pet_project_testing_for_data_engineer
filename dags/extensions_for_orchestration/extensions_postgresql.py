from typing import Any

import airflow.models.connection

from airflow.providers.postgres.hooks.postgres import PostgresHook
from extensions_for_orchestration.extensions_dict import dict_keys_in_placeholder
from extensions_for_orchestration.extensions_dict import dict_keys_in_str
from extensions_for_orchestration.extensions_str import generate_insert_into_for_row


def save_dict_to_postgres(
    conn_id: str | None = "dwh",
    schema: str | None = "public",
    table: str | None = None,
    dict_row: dict[str, Any] | None = None,
) -> None:
    """
    Универсальная функция для вставки одной строки в любую таблицу (Postgres).
    :param conn_id: Название соединения Airflow
    :param schema: Схема Postgres
    :param table: Имя таблицы
    :param dict_row: Произвольный dict со значениями для вставки (названия ключей = поля таблицы)
    """
    pg_hook = PostgresHook(postgres_conn_id=conn_id)

    if not dict_row:
        raise ValueError("Нет данных для вставки (пустой словарь)")

    if isinstance(conn_id, airflow.models.connection.Connection):
        pg_hook = PostgresHook(postgres_conn_id=None, connection=conn_id)

    columns = dict_keys_in_str(source_dict=dict_row)
    placeholders = dict_keys_in_placeholder(source_dict=dict_row)
    insert_sql = generate_insert_into_for_row(schema=schema, table=table, columns=columns, placeholders=placeholders)

    pg_hook.run(sql=insert_sql, parameters=dict_row, autocommit=True)


# conn_params = {
#     "host": "localhost",
#     "schema": "postgres",
#     "login": "postgres",
#     "password": "postgres",
#     "port": 5433,
# }

# Создание объекта подключения вручную
# conn = Connection(
#     conn_type="postgres",
#     host=conn_params["host"],
#     schema=conn_params["schema"],
#     login=conn_params["login"],
#     password=conn_params["password"],
#     port=conn_params["port"],
# )

# print(type(conn))
#
# if isinstance(conn, airflow.models.connection.Connection):
#     print("yes")
# else:
#     print('not yes')

# save_dict_to_postgres(
#     conn_id=conn, table="users", row={"first_name": "Ivan", "last_name": "Ivanov", "email": "foo@example.com"}
# )
