import pytest
from src.generators import filter_by_currency,transaction_descriptions, card_number_generator

    @pytest.mark.parametrize("transaction, expected_result", [
        ('70007922896063611', 'Номер карты должен состоять не более чем из 16 цифр.'),
        ('700079228960636', 'Номер карты должен состоять не менее чем из 16 цифр.'),
        ('', 'Номер карты не введен.'),
        ('7000792289606361', '7000 79XX XXXX 6361'),
        ('7000792289hf6361', 'Номер карты должен состоять только из цифр.'),
        ('1111111111111111', '1111 11XX XXXX 1111')
    ])


    def test_filter_by_currency(transaction, expected_result):
        assert get_mask_card_number(transaction) == expected_result