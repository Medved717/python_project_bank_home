import requests
from src.utils.external_api import covert_to_rub
from unittest.mock import patch, mock_open
from src.utils.external_api import file_path
from src.utils.external_api import operations_json


@patch('builtins.open')
@patch('os.path.exists', return_value=True)
def test_operations_json(mock_exists, mock_file):
    mock_file.return_value.__enter__.return_value.read.return_value = "{}"
    result = operations_json(file_path)
    assert result == []
    mock_file.assert_called_once()


@patch('os.path.exists', return_value=False)
def test_operations_no_exists(mock_exists):
    mock_exists.return_value = False
    result = operations_json(file_path)
    assert result == []
    mock_exists.assert_called_once()


@patch('os.path.exists', return_value=True)
@patch('builtins.open')
@patch('json.load', return_value=[{"id": 873106923, "amount": "43318.34"}])
def test_operations_on(mock_exists, mock_file, mock_open):
    mock_file.return_value.mock_open.return_value.read.return_value.json.load.return_value = [{
    "id": 873106923}, {"amount": "43318.34"}]
    result = operations_json(file_path)
    assert result == [{"id": 873106923, "amount": "43318.34"}]
    mock_exists.assert_called_once()
    mock_file.assert_called_once()
    mock_open.assert_called_once()


@patch("requests.get")
def test_covert_to_rub(mock_requests):
    mock_requests.return_value.json.return_value = {'success': True, 'query': {'from': 'USD', 'to': 'RUB', 'amount': 79114.93},
                                           'info': {'timestamp': 1776172085, 'rate': 75.626607}, 'date': '2026-04-14',
                                           'result': 5983193.718943}

    result =  covert_to_rub({
    "id": 142264268,
    "state": "EXECUTED",
    "date": "2019-04-04T23:20:05.206878",
    "operationAmount": {
      "amount": "79114.93",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод со счета на счет",
    "from": "Счет 19708645243227258542",
    "to": "Счет 75651667383060284188"
  })
    assert result == 5983193.718943
    mock_requests.assert_called_once()


@patch("requests.get")
def test_covert_to_rub_no_internet(mock_requests_get):
    # Имитируем ошибку соединения
    mock_requests_get.side_effect = requests.exceptions.ConnectionError("No internet")

    # Тестовая транзакция в USD
    transaction = {
        "operationAmount": {
            "amount": "100.00",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }
    }

    result = covert_to_rub(transaction)
    assert result == 0.0
    mock_requests_get.assert_called_once()


