import logging

from sqlalchemy import create_engine
from sqlalchemy import text


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def execute_custom_query_postgres(  # noqa: PLR0913
    db_name: str | None = "postgres",
    host: str = "localhost",
    user: str = "postgres",
    password: str = "postgres",  # noqa: S107
    port: int = 5432,
    query: str | None = None,
) -> None:
    """
    Выполнение произвольного запроса в PostgreSQL.

    :param db_name: Имя базы данных.
    :param host: Хост базы данных.
    :param user: Пользователь базы данных.
    :param password: Пароль пользователя базы данных.
    :param port: Порт базы данных.
    :param query: Запрос для выполнения.
    :return: None
    """

    # Подключаемся к БД postgres (системная БД)
    engine = create_engine(url=f"postgresql://{user}:{password}@{host}:{port}/{db_name}", isolation_level="AUTOCOMMIT")

    # Выполняем пользовательский запрос
    with engine.connect() as connection:
        connection.execute(text(query))
        logging.info(f"✅ Запрос успешно выполнен: {query}")
    engine.dispose()


# Пример использования
if __name__ == "__main__":
    pass
