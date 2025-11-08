from create_connection import create_airflow_connection


if __name__ == "__main__":
    create_airflow_connection(
        connection_id="dwh",
        host="dwh",
        user_name="airflow",
        password_auth="airflow",  # noqa: S106
    )
