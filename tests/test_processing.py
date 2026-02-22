import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state() -> None:
    "Тест для проверки ошибки на введение (получение) пустого списка."
    with pytest.raises(ValueError):
        filter_by_state([])


def test_filter_by_state_no_state(transactions: list) -> None:
    'Тест на проверку отсутствия ключа "state"'
    with pytest.raises(KeyError):
        filter_by_state(transactions)


def test_sort_by_no_list() -> None:
    "Тест для проверки ошибки на введение (получение) пустого списка."
    with pytest.raises(ValueError):
        filter_by_state([])


def test_sort_by_date(date: list) -> None:
    'Тест на проверку отсутствия ключа "date"'
    with pytest.raises(KeyError):
        sort_by_date(date)
