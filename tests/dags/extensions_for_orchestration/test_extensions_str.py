from extensions_for_orchestration.extensions_postgresql import generate_insert_into_for_row


class TestGenerateInsertIntoForRow:
    def test_standard_query(self):
        result = generate_insert_into_for_row(
            schema="public",
            table="users",
            columns="id, name, email",
            placeholders="%(id)s, %(name)s, %(email)s",
        )
        assert result == "INSERT INTO public.users (id, name, email) VALUES (%(id)s, %(name)s, %(email)s)"

    def test_custom_schema(self):
        result = generate_insert_into_for_row(
            schema="analytics",
            table="metrics",
            columns="metric_name, metric_value",
            placeholders="%(metric_name)s, %(metric_value)s",
        )
        assert result == (
            "INSERT INTO analytics.metrics (metric_name, metric_value) VALUES (%(metric_name)s, %(metric_value)s)"
        )

    def test_no_schema(self):
        # schema=None, should behave as string "None"
        result = generate_insert_into_for_row(
            schema=None,
            table="table",
            columns="a",
            placeholders="%(a)s",
        )
        assert result == "INSERT INTO None.table (a) VALUES (%(a)s)"

    def test_no_table(self):
        # table=None, should behave as string "None"
        result = generate_insert_into_for_row(
            schema="sch",
            table=None,
            columns="a",
            placeholders="%(a)s",
        )
        assert result == "INSERT INTO sch.None (a) VALUES (%(a)s)"

    def test_none_columns_and_placeholders(self):
        # columns and placeholders None → "None" and "None"
        result = generate_insert_into_for_row(schema="s", table="t", columns=None, placeholders=None)
        assert result == "INSERT INTO s.t (None) VALUES (None)"
