def generate_insert_into_for_row(
    schema: str | None = "public",
    table: str | None = None,
    columns: str | None = None,
    placeholders: str | None = None
) -> str:
    """
    
    :param schema:
    :param table:
    :param columns:
    :param placeholders:
    :return:
    """
    return f"INSERT INTO {schema}.{table} ({columns}) VALUES ({placeholders})"
