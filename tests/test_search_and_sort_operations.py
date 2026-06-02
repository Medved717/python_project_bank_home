from src.search_and_sort_operations import counter_bank_operations, process_bank_search


def test_process_bank_search(transactions_1):
    """Тест по проверке поиска строк по словарям."""

    result = process_bank_search(transactions_1, 'Перевод')
    assert len(result) == 5


def test_process_bank_search_empty_list():
    """Тест по проверке пустого входного списка."""

    result = process_bank_search([], 'Перевод')
    assert result == []


def test_process_bank_search_empty_str(transactions_1):
    """Тест по проверке пустого поиска строк по словарям."""

    result = process_bank_search(transactions_1, '')
    assert result == transactions_1


def test_counter_bank_operations(transactions_1):
    """Тест по проверке количества совпадений поиска по введенному слову."""

    result = counter_bank_operations(transactions_1, '[Перевод, организации]')
    assert len(result) == 3


def test_counter_bank_operations_empty_str(transactions_1):
    """Тест по проверке количества совпадений поиска по введенному слову."""

    result = counter_bank_operations(transactions_1, '[]')
    assert len(result) == 0
