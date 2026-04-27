import json
import os
import requests
from dotenv import load_dotenv

file_path = os.path.join('..', '..', 'data', 'operations.json')


def operations_json(json_file: str) -> list:
    '''Осуществляется прием json файла со списком транзакций, обрабатывается и выводит список транзакций
    в виде списка словарей.'''

    if not os.path.exists(json_file):
        return []
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if len(data) == 0:
                return []
    except json.JSONDecodeError:
        return []
    return data


load_dotenv()
api_kei = os.getenv("API_KEY")

def covert_to_rub(list_transactions: dict) -> float:
    """Вывод суммы транзакции в рублях или конвертация
       суммы из различных валют: USD, EUR."""

    currency_code = list_transactions["operationAmount"]["currency"]["code"]
    amount = float(list_transactions["operationAmount"]["amount"])
    try:
        if currency_code != "RUB":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
            headers = {
                "apikey": api_kei
            }
            response = requests.get(url, headers=headers)
            response_json = response.json()
            converted_amount = response_json["result"]
            return float(converted_amount)
        else:
            return amount
    except requests.exceptions.RequestException:
        print("Возникла ошибка!")
        return 0.0

print(covert_to_rub({
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
  }))