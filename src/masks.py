import logging
import os

# Поднимаемся на уровень выше из src в корень проекта
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logs_path = os.path.join(project_root, "logs", "logger_masks.log")

logger = logging.getLogger("logger_masks")
file_handler = logging.FileHandler(logs_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s, %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    logger.info("Проверяем условия соответствия номера карты.")
    if not card_number:
        return "Номер карты не введен."
    if len(card_number) > 16:
        return "Номер карты должен состоять не более чем из 16 цифр."
    if len(card_number) < 16:
        return "Номер карты должен состоять не менее чем из 16 цифр."
    if not card_number.isdigit():
        return "Номер карты должен состоять только из цифр."
    else:
        logger.info("Ведется формирование номера карты в соответствиями с требованиями.")
        mask_number = card_number[:6] + "XXXXXX" + card_number[12:]
        groups = []
        logger.info("Приводим номер карты к соответствующему образцу вывода.")
        for i in range(0, len(mask_number), 4):
            group = mask_number[i: i + 4]
            groups.append(group)
        logger.info("Выводим результат номера карты, приведенного в соответствие.")
        result = " ".join(groups)
        return result


get_mask_card_number("2345347865435679")


def get_mask_account(mask_account: str) -> str:
    """ "Функция, которая укорачивает и маскирует номер счета"""
    logger.info("Проверяем соответствие номера счета критериям.")
    if not mask_account:
        return "Вы не ввели номер счета."
    if len(mask_account) > 20:
        return "Номер счета должен состоять не более чем из 20 цифр."
    if len(mask_account) < 20:
        return "Номер счета должен состоять не менее чем из 20 цифр."
    if not mask_account.isdigit():
        return "Номер счета должен состоять только из цифр."
    else:
        logger.info(
            "Проверка соответствия номера счета пройдена, проводится редактирования номера карты" "для вывода."
        )
        new_mask_account = mask_account[-6:]
        result = new_mask_account.replace(new_mask_account[0:2], "**")
        logger.info("Выполнение формирования номера счета завершена.")
        return result


get_mask_account("34543678756894567467")
