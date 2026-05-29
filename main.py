from src.processing import filter_by_state
from src.read_csv_and_excel_files import reading_csv_transactions, reading_excel_transactions
from src.utils.external_api import operations_json

if __name__ == '__main__':

    print('Программа: Привет! Добро пожаловать в программу работы '
          'с банковскими транзакциями. ')
    print('Выберите необходимый пункт меню:\n'
          '1. Получить информацию о транзакциях из JSON-файла\n'
          '2. Получить информацию о транзакциях из CSV-файла\n'
          '3. Получить информацию о транзакциях из XLSX-файла')

    while True:
        input_word = input('Пользователь:')
        if input_word == '1':
            operation_data = operations_json('data/operations.json')
            print('Программа: Для обработки выбран JSON-файл.')
            break
        elif input_word == '2':
            operation_data = reading_csv_transactions('data/transactions.csv')
            print('Программа: Для обработки выбран CSV-файл.')
            break
        elif input_word == '3':
            operation_data = reading_excel_transactions('data/transactions_excel.xlsx')
            print('Программа: Для обработки выбран EXCEL-файл.')
            break
        else:
            print('Данного пункта нет в меню.')

    print('Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n'
          'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

    while True:
        input_word = input('Пользователь:').upper()
        if input_word == 'EXECUTED':
            filter_data = filter_by_state(operation_data)
            print('Программа: Операции отфильтрованы по статусу "EXECUTED"')
            break
        elif input_word == 'CANCELED':
            filter_data = filter_by_state(operation_data, 'CANCELED')
            print('Программа: Операции отфильтрованы по статусу "CANCELED"')
            break
        elif input_word == 'PENDING':
            filter_data = filter_by_state(operation_data, 'PENDING')
            print('Программа: Операции отфильтрованы по статусу "PENDING"')
            break
        else:
            print(f'Программа: Статус операции {input_word} недоступен.')
            print('Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n'
                  'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')


