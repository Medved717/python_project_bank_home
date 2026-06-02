import json
import logging
import os

import requests
from dotenv import load_dotenv

# Поднимаемся на уровень выше из src в корень проекта
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
logs_path = os.path.join(project_root, "logs", "external_log.log")


logger = logging.getLogger("external_log")
file_handler = logging.FileHandler(logs_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s, %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def operations_json(json_file: str) -> list:
    """Осуществляется прием json файла со списком транзакций, обрабатывается и выводит список транзакций
    в виде списка словарей."""

    if not os.path.exists(json_file):
        return []
    try:
        logger.info(
            "Осуществляется прием json файла со списком транзакций, "
            "обрабатывается и выводит список транзакций в виде списка словарей."
        )
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if len(data) == 0:
                return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка парсинга JSON: {e}")
        return []
    except IOError as e:
        logger.error(f"Ошибка чтения файла: {e}")
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
        logger.info("Идет процесс получения сведений по курсам валют.")
        if currency_code != "RUB":
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
            headers = {"apikey": api_kei}
            response = requests.get(url, headers=headers)
            response_json = response.json()
            converted_amount = response_json["result"]
            logger.info("Получены сведения по курсам валют.")
            return float(converted_amount)
        else:
            logger.info("Выведена сумма в рублях без перевода курса валют.")
            return amount
    except requests.exceptions.RequestException as e:
        logger.error(f"Возникла ошибка при выведении суммы. Ошибка: {e}")
        print("Возникла ошибка!")
        return 0.0


# print(
#     covert_to_rub(
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188",
#         }
#     )
# )
