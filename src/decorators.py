import datetime
from functools import wraps


def log(filename=None):
    """Декоратор, который осуществляет логирование функции
    по записи имени функции, её аргументов и возможных ошибок"""

    def wrapped(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = datetime.datetime.now()
            result = None
            try:
                result = func(*args, **kwargs)
                log_message = f"Имя функции: {func.__name__}, выполнено"
            except Exception as e:
                log_message = f"Имя функции: {func.__name__}, Ошибка: {e}, аргументы {args, kwargs}"
            end_time = datetime.datetime.now()
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(f"{start_time}, {end_time}, {log_message}\n")
            else:
                print(f"{start_time}, {end_time}, {log_message}")
            return result

        return inner

    return wrapped
