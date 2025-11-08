from typing import Any, Dict


def extract_user_fields(api_response: Dict[str, Any]) -> Dict[str, str]:
    """
    Извлекает нужные пользовательские данные из полной структуры API randomuser.me.

    :param api_response: Ответ (dict), полученный из API
    :return: Словарь с user-полями: first_name, last_name, email, city, country
    :raises KeyError: если структура отличается от ожидаемой
    """
    user = api_response["results"][0]
    return {
        "first_name": user["name"]["first"],
        "last_name": user["name"]["last"],
        "email": user["email"],
        "city": user["location"]["city"],
        "country": user["location"]["country"],
    }
