# from airflow.models.connection import Connection
from airflow.providers.postgres.hooks.postgres import PostgresHook


def test_postgres_connection():  # noqa: D103
    # conn = Connection(
    #        conn_type="postgres", host="localhost", schema="postgres", login="postgres", password="postgres", port=5434
    #     )
    # hook = PostgresHook(postgres_conn_id=None, connection=conn)
    hook = PostgresHook(postgres_conn_id="dwh")

    conn = hook.get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT 1")
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    assert result == (1,)
