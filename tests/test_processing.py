import pytest
from example.processing1 import filter_by_state

def test_filter_by_state():
    with pytest.raises(ValueError) as exc_info:
        filter_by_state([])


def test_filter_by_state_no_state(transactions):
    with pytest.raises(KeyError) as exc_info:
        filter_by_state(transactions)
