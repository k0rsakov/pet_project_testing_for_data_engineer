import pytest
from extensions_for_orchestration.extensions_dict import (
    dict_keys_in_str,
    dict_keys_in_placeholder,
)


class TestDictKeysInStr:
    def test_empty_dict(self):
        assert dict_keys_in_str({}) == ""

    @pytest.mark.unit
    def test_none(self):
        assert dict_keys_in_str(None) == ""

    def test_single_key(self):
        d = {"a": 1}
        assert dict_keys_in_str(d) == "a"

    def test_multiple_keys(self):
        d = {"name": "Vasya", "age": 23, "country": "RU"}
        assert dict_keys_in_str(d) == "name, age, country"


class TestDictKeysInPlaceholder:
    def test_empty_dict(self):
        assert dict_keys_in_placeholder({}) == ""

    def test_none(self):
        assert dict_keys_in_placeholder(None) == ""

    def test_single_key(self):
        d = {"id": 42}
        assert dict_keys_in_placeholder(d) == "%(id)s"

    def test_multiple_keys(self):
        d = {"name": "Ivan", "age": 30, "city": "Tomsk"}
        assert dict_keys_in_placeholder(d) == "%(name)s, %(age)s, %(city)s"
