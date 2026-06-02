import os

import pandas as pd

transactions_puth_csv = os.path.join("../data/transactions.csv")


def reading_csv_transactions(transactions_puth_csv):
    """Прием транзакций в формате csv и возвращение списка словарей."""
    df_transactions_csv = pd.read_csv(transactions_puth_csv, sep=";", skipinitialspace=True)
    transactions_dict = df_transactions_csv.to_dict("records")
    return transactions_dict


transactions_puth_excel = os.path.join("../data/transactions_excel.xlsx")


def reading_excel_transactions(transactions_puth_excel):
    """Прием транзакций в формате excel и возвращение списка словарей."""

    df_transactions_csv = pd.read_excel(transactions_puth_excel)
    transactions_dict = df_transactions_csv.to_dict("records")
    return transactions_dict
