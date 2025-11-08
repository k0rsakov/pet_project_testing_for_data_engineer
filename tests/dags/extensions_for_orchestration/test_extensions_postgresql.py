import pandas as pd
import pytest
from unittest.mock import patch, MagicMock
from airflow.models.connection import Connection
from extensions_for_orchestration.extensions_postgresql import save_dict_to_postgres
from handles.oltp.execute_custom_query import execute_custom_query_postgres
from airflow.providers.postgres.hooks.postgres import PostgresHook


class TestSaveDictToPostgres:
    def create_test_users(self):
        execute_custom_query_postgres(
            port=5434,
            query="""
                DROP TABLE IF EXISTS users;

                CREATE TABLE users (
                    user_id bigserial PRIMARY KEY,
                    created_at timestamptz NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    first_name text NULL,
                    last_name text NULL,
                    email text NULL,
                    city text NULL,
                    country text NULL
                );
                """,
        )

    def create_pg_conn(self):
        return Connection(
            conn_type="postgres", host="localhost", schema="postgres", login="postgres", password="postgres", port=5434
        )

    def test_example_use_extension(self):
        conn = self.create_pg_conn()
        self.create_test_users()
        save_dict_to_postgres(
            conn_id=conn,
            table="users",
            dict_row={
                "first_name": "Ivan",
                "last_name": "Ivanov",
                "email": "foo@example.com",
                "city": "Irkutsk",
                "country": "Russia",
            },
        )
        pg_hook = PostgresHook(postgres_conn_id=None, connection=conn)

        df = pg_hook.get_records(
            sql="select * from users",
        )

        print(df)
