def filter_by_state(list_of_transactions: list, status: str = "EXECUTED") -> list:
    """Функция принимает список словарей и выдает новый список словарей,
    в которых присутствует значение 'EXECUTED'."""

    if list_of_transactions == []:
        raise ValueError("Ошибка! Данные отсутствуют.")

    list_executed = []
    for list_state in list_of_transactions:
        if not list_state or "state" not in list_state:
            continue
        if list_state["state"] == status:
            list_executed.append(list_state)
    if list_executed == []:
        return "Отсутствуют данные о state (государстве)."
    else:
        return list_executed


def sort_by_date(filter_date: list[dict], sorted_list: bool = True) -> list[dict]:
    """Функция, которая сортирует список словарей по дате в порядке убывания."""

    if not filter_date:
        raise ValueError("Ошибка! Данные отсутствуют.")
    for date_list in filter_date:
        if "date" not in date_list:
            raise KeyError("Отсутствуют данные по дате!")

    result = sorted(filter_date, key=lambda x: x["date"], reverse=sorted_list)
    return result
