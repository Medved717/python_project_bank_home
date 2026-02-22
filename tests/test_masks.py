import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_card, expected_result",
    [
        ("70007922896063611", "Номер карты должен состоять не более чем из 16 цифр."),
        ("700079228960636", "Номер карты должен состоять не менее чем из 16 цифр."),
        ("", "Номер карты не введен."),
        ("7000792289606361", "7000 79XX XXXX 6361"),
        ("7000792289hf6361", "Номер карты должен состоять только из цифр."),
        ("1111111111111111", "1111 11XX XXXX 1111"),
    ],
)
def test_get_mask_card_number(number_card: str, expected_result: str) -> None:
    assert get_mask_card_number(number_card) == expected_result


@pytest.mark.parametrize(
    "number_account, expected_result",
    [
        ("", "Вы не ввели номер счета."),
        ("736541084301358743051", "Номер счета должен состоять не более чем из 20 цифр."),
        ("7365410843013587430", "Номер счета должен состоять не менее чем из 20 цифр."),
        ("7005467079gh89606361", "Номер счета должен состоять только из цифр."),
        ("73654108430135874f305", "Номер счета должен состоять не более чем из 20 цифр."),
        ("736541084301358f305", "Номер счета должен состоять не менее чем из 20 цифр."),
    ],
)
def test_get_mask_account(number_account: str, expected_result: str) -> None:
    assert get_mask_account(number_account) == expected_result
