import logging

from airflow.models.connection import Connection
from extensions_for_orchestration.extensions_postgresql import save_dict_to_postgres
from handles.oltp.execute_custom_query import execute_custom_query_postgres
from airflow.providers.postgres.hooks.postgres import PostgresHook


class TestSaveDictToPostgres:
    @staticmethod
    def create_test_users():
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

    @staticmethod
    def create_pg_conn():
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

        list_ = pg_hook.get_records(
            sql="select * from users",
        )

        logging.info(*list_)

        # assert len(list_) == 1
        assert len(list_) == 2
