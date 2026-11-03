# === Stage 1: Каркас модуля ===
# Project: PowerBills
from dataclasses import dataclass, field
from datetime import date
from typing import List


@dataclass
class Account:
    period: date
    tariff: str
    consumption: float
    amount: float


def make_demo_accounts() -> List[Account]:
    accounts = [
        Account(date(2024, 1, 1), "дневной", 120.5, 1807.5),
        Account(date(2024, 1, 2), "ночной", 45.2, 542.4),
        Account(date(2024, 1, 3), "пиковый", 88.0, 968.0),
    ]
    return accounts


def main() -> None:
    accounts = make_demo_accounts()
    print("Демо-счета за электричество:")
    for account in accounts:
        print(f"  Период: {account.period}, тариф: {account.tariff}, "
              f"расход: {account.consumption} кВт·ч, сумма: {account.amount} руб.")


if __name__ == "__main__":
    main()
