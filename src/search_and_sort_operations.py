import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)->list[dict]:
    """Принимет список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""

    pattern = re.compile(search, re.IGNORECASE)
    sort_data = []
    for item in data:
        for values in item.values():
            search_by_word = pattern.findall(values)
            if search_by_word:
                sort_data.append(item)
                break
    return sort_data


def process_bank_operations(data:list[dict], categories:list)->dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    list_operations = []
    for item in data:
        if item['description'] in categories:
            list_operations.append(item['description'])
    category_count = Counter(list_operations)
    return category_count









