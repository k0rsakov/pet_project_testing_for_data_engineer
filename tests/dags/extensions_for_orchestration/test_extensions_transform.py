import pytest
from dags.extensions_for_orchestration.extensions_transform import extract_nested_fields


class TestExtractNestedFields:
    def test_normal_data(self):
        user_data = {
            "results": [
                {
                    "name": {"first": "Ivan", "last": "Petrov"},
                    "email": "ivan.petrov@example.com",
                    "location": {"city": "Moscow", "country": "RU"},
                }
            ]
        }
        result = extract_nested_fields(user_data)
        assert result == {
            "first_name": "Ivan",
            "last_name": "Petrov",
            "email": "ivan.petrov@example.com",
            "city": "Moscow",
            "country": "RU",
        }

    def test_missing_field(self):
        # city отсутствует
        user_data = {
            "results": [
                {
                    "name": {"first": "Anna", "last": "Smith"},
                    "email": "anna.smith@example.com",
                    "location": {"country": "DE"},
                }
            ]
        }
        with pytest.raises(KeyError):
            extract_nested_fields(user_data)

    def test_empty_results(self):
        user_data = {"results": []}
        with pytest.raises(IndexError):
            extract_nested_fields(user_data)

    def test_none_argument(self):
        with pytest.raises(TypeError):
            extract_nested_fields(None)
