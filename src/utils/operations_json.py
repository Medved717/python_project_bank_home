import os
import json



file_path = os.path.join('..', '..', 'data', 'operations.json')


def operations_json(json_file: str) -> list:
    '''Осуществляется прием json файла со списком транзакций, обрабатывается и выводит список транзакций
    в виде списка словарей.'''

    if not os.path.exists(json_file):
        return []

    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            json_file_read = f.read()

            if len(json_file_read) == 0:
                return []

            else:
                data = json.load(f)

    except json.JSONDecodeError:
        return []

    return data


result = operations_json(file_path)
print(result)
