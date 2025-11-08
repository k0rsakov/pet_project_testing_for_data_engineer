def return_only_int_value(value: int | None = None) -> int | None:
    if value is not None and not isinstance(value, int):
        raise TypeError("value must be int or None")
    return value
