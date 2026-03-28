import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "transaction_state, expected_state",
    [
        (
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
            [{"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}],
        ),
        (
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
            "Отсутствуют данные о state (государстве).",
        ),
        (
            [{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}],
            "Отсутствуют данные о state (государстве).",
        ),
    ],
)
def test_filter_by_state(transaction_state, expected_state):
    result = filter_by_state(transaction_state)
    assert result == expected_state


def test_sort_by_date(date_card, date_card_sort):
    result = sort_by_date(date_card_sort)
    assert result == date_card_sort
