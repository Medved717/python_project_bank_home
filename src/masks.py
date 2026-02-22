def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску."""
    if not card_number:
        return "Номер карты не введен."
    if len(card_number) > 16:
        return "Номер карты должен состоять не более чем из 16 цифр."
    if len(card_number) < 16:
        return "Номер карты должен состоять не менее чем из 16 цифр."
    if not card_number.isdigit():
        return "Номер карты должен состоять только из цифр."
    else:
        mask_number = card_number[:6] + "XXXXXX" + card_number[12:]
        groups = []
        for i in range(0, len(mask_number), 4):
            group = mask_number[i: i + 4]
            groups.append(group)

        result = " ".join(groups)
        return result


def get_mask_account(mask_account: str) -> str:
    """ "Функция, которая укорачивает и маскирует номер счета"""

    if not mask_account:
        return "Вы не ввели номер счета."
    if len(mask_account) > 20:
        return "Номер счета должен состоять не более чем из 20 цифр."
    if len(mask_account) < 20:
        return "Номер счета должен состоять не менее чем из 20 цифр."
    if not mask_account.isdigit():
        return "Номер счета должен состоять только из цифр."
    else:
        new_mask_account = mask_account[-6:]
        result = new_mask_account.replace(new_mask_account[0:2], "**")
        return result
