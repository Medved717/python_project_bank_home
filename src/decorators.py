from optparse import Option
from functools import wraps
import datetime


def log(filename=None):
    '''Декоратор, который осуществляет логирование функции
     по записи имени функции, её аргументов и возможных ошибок'''

    def wrapped(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                log_message = f'Имя функции: {func().__name__}, аргументы функции: {args, kwargs'}, выполнено'
            except Exception as e:
                log_message = f'Имя функции: {func().__name__}, Ошбика: {e}, аргументы {args, kwargs}'
            end_time = datetime.datetime.now()
            if filename:
                with open(filename, 'a') as file:
                    file.write(f'{start_time}, {end_time}, {log_message}\n')
            else:
                print(f'{start_time}, {end_time}, {log_message}')
            return result
        return wrapped





