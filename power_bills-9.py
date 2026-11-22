# === Stage 9: Сортировка записей ===
# Project: PowerBills
from datetime import datetime


def parse_period(period):
    return datetime.strptime(str(period), "%Y-%m-%d").date()


def sort_records(records, key="period", reverse=False):
    def sort_key(record):
        return (record.get(key), record.get("created_at"))
    return sorted(records, key=sort_key, reverse=reverse)


if __name__ == "__main__":
    sample = [
        {"period": "2024-01-15", "created_at": "2024-01-20T10:00:00", "sum": 100},
        {"period": "2024-01-10", "created_at": "2024-01-18T09:00:00", "sum": 200},
        {"period": "2024-01-10", "created_at": "2024-01-19T11:00:00", "sum": 300},
    ]
    print(sort_records(sample))
