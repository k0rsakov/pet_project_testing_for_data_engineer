from typing import Any, Sequence


def extract_nested_fields(user_data: dict | None = None) -> dict[str, Any]:
    """
    Пример сложной логики для randomuser.me (можно расширять):

    :param user_data: Апи-ответ для одного пользователя (user_data['results'][0])
    :return: Словарь нормализованных user-данных
    """
    user = user_data["results"][0]
    return {
        "first_name": user["name"]["first"],
        "last_name": user["name"]["last"],
        "email": user["email"],
        "city": user["location"]["city"],
        "country": user["location"]["country"],
    }
