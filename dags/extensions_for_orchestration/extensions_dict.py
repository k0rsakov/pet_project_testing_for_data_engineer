from typing import Any


def dict_keys_in_str(source_dict: dict[str, Any] | None = None) -> str:
    """
    Функция, которая генерирует строку с указанными колонками.

    :param source_dict: Словарь, ключи которого необходимо преобразовать в строку; default 'None'
    :return: str с указанными колонками через запятую
    """
    if source_dict is None:
        return ""
    return ", ".join(source_dict.keys())


def dict_keys_in_placeholder(source_dict: dict[str, Any] | None = None) -> str:
    """

    :param source_dict:
    :return:
    """
    if source_dict is None:
        return ""
    return ", ".join([f"%({k})s" for k in source_dict.keys()])
