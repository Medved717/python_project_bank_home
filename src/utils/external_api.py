import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_kei = os.getenv("API_KEY")

def covert_to_rub(list_transactions: dict) -> float:
    '''Вывод суммы транзакции в рублях или конвертация   суммы из разлисных валют: USD, EUR.'''

    currency_code = list_transactions["operationAmount"]["currency"]["code"]
    amount = float(list_transactions["operationAmount"]["amount"])

    if currency_code != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        headers = {
            "apikey": api_kei
        }
        response = requests.get(url, headers=headers).json()
        converted_amount = response["result"]
        return float(converted_amount)
    else:
        return amount


