import requests


def get_api_response(url: str = "https://randomuser.me/api/") -> dict:
    """
    Получает набор данных по пользователей по указанному URL (по умолчанию randomuser.me).

    :param url: URL API (по умолчанию randomuser.me)
    :return: Данные из API в формате dict (response.json())
    :raises Exception: если не получилось получить данные
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Ошибка получения данных: {response.status_code}")
    return response.json()
