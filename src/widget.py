from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def get_mask_account_card(card_and_account_number: str) -> str:
    """Функция, которая принимает на вход тип и номер карты, а также номер счета, выводит маску."""

    if card_and_account_number == "":
        raise ValueError("Ошибка: введена пустая строка.")

    card_types = {"Maestro": 8, "MasterCard": 11, "Visa Classic": 13, "Visa Platinum": 14, "Visa Gold": 10, "МИР": 4}
    score_types = "Счет"
    score_len = 5

    # Создаем условие при котором, если будет задан тип "Счет",
    # то далее осуществляем сокрытие номера счета и присоединяем тип счета.
    if score_types in card_and_account_number:
        number_score = card_and_account_number[score_len:]
        mask_number_score = get_mask_account(number_score)
        result_mask_number_score = score_types + " " + mask_number_score
        return result_mask_number_score

    # Проходим по циклу словаря типов карт и выбирам ту, которая соответствует введенному типу
    # и маскируем номер карты, и присоединяем тип карты
    for card, card_len in card_types.items():
        if card in card_and_account_number:
            card_types_cycle = card_and_account_number[:card_len]
            card_number = card_and_account_number[card_len:].strip(" ")
            mask_card_number = get_mask_card_number(card_number)
            result_mask_card = card_types_cycle + mask_card_number
            return result_mask_card

    raise ValueError("Не удалось распознать тип карты или счета.")


def convert_date(date: str) -> str:
    """Преобразует даты из представленного формата в необходимый формат
    '2018-01-21T01:10:28.317704' → '21.01.2018'"""

    date_obj = datetime.strptime(date[:10], "%Y-%m-%d")
    return date_obj.strftime("%d.%m.%Y")
