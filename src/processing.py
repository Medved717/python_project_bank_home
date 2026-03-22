def filter_by_state(list_of_transactions: list, status: str = "EXECUTED") -> list:
    """Функция, которая принимает список словарей и выдает новый список словарей,
    в которых присутствует значение 'EXECUTED'."""

    list_executed = []
    for list_state in list_of_transactions:
        if list_state["state"] == status:
            list_executed.append(list_state)
    if list_executed == []:
        return "Отсутствуют данные о state (государстве)."
    else:
        return list_executed


# result_excuted = filter_by_state(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# )
# print(result_excuted)


def sort_by_date(filter_date: list[dict], sorted_list: bool = True) -> list[dict]:
    """Функция, которая сортирует список словарей по по дате в порядке убывания."""

    return sorted(filter_date, key=lambda x: x["date"], reverse=sorted_list)


# result_sort = sort_by_date(
#     [
#         {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
#         {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
#         {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
#         {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
#     ]
# )
# print(result_sort)
