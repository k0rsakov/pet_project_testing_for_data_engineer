from typing import Any

import requests


def get_api_response(
    url: str | None = None,
    method: str = "GET",
    params: dict | None = None,
    headers: dict | None = None,
    timeout: int = 30,
) -> Any:
    """
    Универсальная функция для HTTP-запроса к API.

    :param url: URL эндпоинта API
    :param method: HTTP-метод (GET, POST и т.д.), по умолчанию GET
    :param params: Query-параметры для запроса
    :param headers: Заголовки запроса
    :param timeout: Таймаут на запрос в секундах
    :return: Распарсенный JSON (или вызывает исключение, если не получилось получить)
    :raises Exception: при ошибке запроса или если статус-код не 2xx
    """
    response = requests.request(method=method, url=url, params=params, headers=headers, timeout=timeout)
    response.raise_for_status()
    try:
        return response.json()
    except Exception as exc:
        raise Exception(f"Ошибка парсинга JSON из ответа {url}: {exc}") from exc
