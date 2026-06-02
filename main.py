import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.read_csv_and_excel_files import reading_csv_transactions, reading_excel_transactions
from src.search_and_sort_operations import counter_bank_operations, process_bank_search
from src.utils.external_api import operations_json
from src.widget import convert_date, get_mask_account_card

if __name__ == "__main__":

    print("Программа: Привет! Добро пожаловать в программу работы\n " "с банковскими транзакциями. ")
    print(
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла"
    )

    while True:
        input_word = input("Пользователь:")
        if input_word == "1":
            path_json_file = os.path.join("data", "operations.json")
            operation_data = operations_json(path_json_file)
            print("Программа: Для обработки выбран JSON-файл.")
            break
        elif input_word == "2":
            path_csv_file = os.path.join("data", "transactions.csv")
            operation_data = reading_csv_transactions(path_csv_file)
            print("Программа: Для обработки выбран CSV-файл.")
            break
        elif input_word == "3":
            path_excel_file = os.path.join("data", "transactions_excel.xlsx")
            operation_data = reading_excel_transactions(path_excel_file)
            print("Программа: Для обработки выбран EXCEL-файл.")
            break
        else:
            print("Данного пункта нет в меню.")

    print(
        "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )

    while True:
        input_word = input("Пользователь:").upper()
        if input_word == "EXECUTED":
            filter_data = filter_by_state(operation_data)
            print('Программа: Операции отфильтрованы по статусу "EXECUTED"')
            break
        elif input_word == "CANCELED":
            filter_data = filter_by_state(operation_data, "CANCELED")
            print('Программа: Операции отфильтрованы по статусу "CANCELED"')
            break
        elif input_word == "PENDING":
            filter_data = filter_by_state(operation_data, "PENDING")
            print('Программа: Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f"Программа: Статус операции {input_word} недоступен.")
            print(
                "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )

    print("Программа: Отсортировать операции по дате? Да/Нет")

    while True:
        input_word = input("Пользователь").upper()
        if input_word == "ДА":
            print("Программа: Отсортировать по возрастанию или по убыванию?")
            input_word = input("Пользователь:").lower()
            if input_word == "по убыванию":
                sort_date = sort_by_date(filter_data)
                break
            elif input_word == "по возрастанию":
                sort_date = sort_by_date(filter_data, False)
                break
        elif input_word == "НЕТ":
            sort_date = filter_data
            break

    print("Программа: Выводить только рублевые транзакции? Да/Нет")

    while True:
        input_word = input("Пользователь:").upper()
        if input_word == "ДА":
            sort_rub = list(filter_by_currency(sort_date, "RUB"))
            break
        elif input_word == "НЕТ":
            sort_rub = sort_date
            break

    print("Программа: Отфильтровать список транзакций \n" "по определенному слову в описании? Да/Нет")

    while True:
        input_word = input("Пользователь:").upper()
        if input_word == "ДА":
            input_search_word = input("Введите искомое слово:")
            search_operation = process_bank_search(sort_rub, input_search_word)
            counter_operation = counter_bank_operations(search_operation, [input_search_word])
            counter_operation_summ = sum(counter_operation.values())
            break
        elif input_word == "НЕТ":
            search_operation = sort_rub
            counter_operation_summ = len(search_operation)
            break

    print("Программа: Распечатываю итоговый список транзакций...")
    print(f"Программа: Всего банковских операций в выборке: {counter_operation_summ}.")

    mask_result = []
    for transaction in search_operation:
        if transaction.get("from"):
            transaction["from"] = get_mask_account_card(transaction["from"])

        if transaction.get("to"):
            transaction["to"] = get_mask_account_card(transaction["to"])

        mask_result.append(transaction)

    formated_date_result = []
    for date in mask_result:
        date["date"] = convert_date(date["date"])
        formated_date_result.append(date)

    for result in formated_date_result:
        print(
            f'{result.get("date")} {result.get("description")}\n'
            f'{result.get("from")} -> {result.get("to")}\n'
            f'Сумма: {result.get("operationAmount").get("amount")}'
            f' {result.get("operationAmount").get("currency").get("name")}'
        )
        print()
