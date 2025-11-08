from handles.oltp.execute_custom_query import execute_custom_query_postgres


if __name__ == "__main__":
    execute_custom_query_postgres(
        port=5433,
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
