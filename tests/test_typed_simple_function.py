import pytest
from main.typed_simple_function import return_only_int_value


def test_with_int():
    assert return_only_int_value(42) == 42


def test_with_none():
    assert return_only_int_value(None) is None


def test_with_str_raises():
    with pytest.raises(TypeError):
        return_only_int_value("not an int")


def test_with_float_raises():
    with pytest.raises(TypeError):
        return_only_int_value(3.14)


def test_with_list_raises():
    with pytest.raises(TypeError):
        return_only_int_value([1, 2, 3])


def test_default_value_is_none():
    assert return_only_int_value() is None
