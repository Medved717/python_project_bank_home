import pytest

from src.widget import get_mask_account_card


@pytest.mark.parametrize(
    "number_and_name_card, expected_result",
    [
        ("Maestrh 7000792289606361", "Не удалось распознать тип карты или счета."),
        ("Masterdard 7000792289606361", "Не удалось распознать тип карты или счета."),
        ("Visa Clafcic 7000792289606361", "Не удалось распознать тип карты или счета."),
        ("Visa Platonum 7000792289606361", "Не удалось распознать тип карты или счета."),
        ("Visa Gpld 7000792289606361", "Не удалось распознать тип карты или счета."),
        ("Счот 70007922896063615683", "Не удалось распознать тип карты или счета."),
    ],
)
def test_mask_account_card_type(number_and_name_card: str, expected_result: str) -> None:
    "Тест обработки не существующих карт и счетов."
    with pytest.raises(ValueError) as exc_info:
        get_mask_account_card(number_and_name_card)
    assert expected_result in str(exc_info.value)


def test_mask_account_card() -> None:
    with pytest.raises(ValueError) as exc_info:
        get_mask_account_card("")
    assert str(exc_info.value) == "Ошибка: введена пустая строка."
