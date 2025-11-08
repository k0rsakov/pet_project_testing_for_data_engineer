from main.simple_function import return_value


def test_return_value_int():
    assert return_value(5) == 5


def test_return_value_str():
    assert return_value("hello") == "hello"
