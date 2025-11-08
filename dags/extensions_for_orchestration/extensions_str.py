def generate_insert_into_for_row(
    schema: str | None = "public", table: str | None = None, columns: str | None = None, placeholders: str | None = None
) -> str:
    """
    Функция для генерации запроса на вставку значений в PostgreSQL.

    :param schema: Схема Postgres
    :param table: Имя таблицы
    :param columns: Колонки для вставки.
    :param placeholders: Колонки обёрнутые в плейсхолдеры.
    :return: Возвращает сгенерированный запрос.
    """
    return f"INSERT INTO {schema}.{table} ({columns}) VALUES ({placeholders})"
