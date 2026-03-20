def filter_by_currency(transactions, code):
    """Фильтрует поступающие транзакции по валюте."""
    found = False
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code", "Транзакция в указанной валюте не найдена.")
            == code
        ):
            found = True
            yield transaction
    if not found:
        yield "Отсутствуют данные о коде валюты."


def transaction_descriptions(transactions):
    """Выводит результат операции."""

    for transaction in transactions:
        if transaction.get("description") is not None:
            yield transaction.get("description")
        else:
            yield "Отсутствуют данные об описании транзакции."


def card_number_generator(start, stop):
    "Генерирует номер карты в заданном периоде."

    for num in range(start, stop + 1):
        str_num = "0" * (16 - len(str(num))) + str(num)
        groups_num = " ".join(list(str_num[i: i + 4] for i in range(0, len(str_num), 4)))
        yield groups_num
