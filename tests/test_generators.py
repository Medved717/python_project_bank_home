from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions):
    """Проверяем транзакцию в валюте "USD"."""
    result = filter_by_currency(transactions, "USD")
    try:
        assert next(result) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
        assert next(result) == {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        }
        assert next(result) == {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        }
    except StopIteration:
        assert False, "Генератор вернул меньше транзакций, чем должно быть."


def test_test_filter_by_currency_not_usd(transactions_rub):
    result_rub = filter_by_currency(transactions_rub, "USD")
    assert next(result_rub) == "Отсутствуют данные о коде валюты."


def test_description(transactions, description):
    """Проверяет вывод описаний транзакций."""

    result = list(transaction_descriptions(transactions))
    assert result == description


def test_card_number_generator(number_card):
    """Проверяет верность генерации номеров карт."""

    assert list(card_number_generator(1, 5)) == number_card
