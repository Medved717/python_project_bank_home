from unittest.mock import patch

import pandas as pd

from src.read_csv_and_excel_files import reading_csv_transactions, reading_excel_transactions


@patch("pandas.read_csv")
def test_reading_csv_transactions(mock_read_csv):
    """Тест проверки поступления данных из файла формата csv и вывода списка словарей."""

    file_path = "transactions.csv"
    test_data = pd.DataFrame(
        [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    mock_read_csv.return_value = test_data
    expected_result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert reading_csv_transactions(file_path) == expected_result
    mock_read_csv.assert_called_once()


@patch("pandas.read_excel")
def test_reading_excel_transactions(mock_read_excel):
    """Тест проверки поступления данных из файла формата excel и вывода списка словарей."""

    file_path = "transactions_excel.xlsx"
    test_data = pd.DataFrame(
        [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    mock_read_excel.return_value = test_data
    expected_result = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    assert reading_excel_transactions(file_path) == expected_result
    mock_read_excel.assert_called_once()
