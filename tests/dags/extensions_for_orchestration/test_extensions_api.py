import pytest
from unittest.mock import patch, MagicMock
from extensions_for_orchestration.extensions_api import get_api_response


class TestGetApiResponse:
    @patch("extensions_for_orchestration.extensions_api.requests.request")
    def test_successful_get(self, mock_request):
        # Подготавливаем mock-ответ
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"status": "ok", "data": [1, 2, 3]}
        mock_request.return_value = mock_response

        url = "https://example.com/api"
        result = get_api_response(url)

        mock_request.assert_called_once_with(method="GET", url=url, params=None, headers=None, timeout=30)
        assert result == {"status": "ok", "data": [1, 2, 3]}

    @patch("extensions_for_orchestration.extensions_api.requests.request")
    def test_http_error(self, mock_request):
        # raise_for_status выбрасывает исключение
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = Exception("404 Not Found")
        mock_request.return_value = mock_response

        with pytest.raises(Exception) as excinfo:
            get_api_response(url="https://bad.url")
        assert "404 Not Found" in str(excinfo.value)

    @patch("extensions_for_orchestration.extensions_api.requests.request")
    def test_json_parse_error(self, mock_request):
        # json() выбрасывает исключение
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.side_effect = ValueError("Not a JSON")
        mock_request.return_value = mock_response

        with pytest.raises(Exception) as excinfo:
            get_api_response(url="https://bad-json.url")
        assert "Ошибка парсинга JSON" in str(excinfo.value)

    @patch("extensions_for_orchestration.extensions_api.requests.request")
    def test_post_with_params_and_headers(self, mock_request):
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"result": "ok"}
        mock_request.return_value = mock_response

        url = "https://api.site/post"
        params = {"q": "search"}
        headers = {"Authorization": "Bearer 123"}
        result = get_api_response(
            url,
            method="POST",
            params=params,
            headers=headers,
            timeout=10,
        )
        mock_request.assert_called_once_with(method="POST", url=url, params=params, headers=headers, timeout=10)
        assert result == {"result": "ok"}
