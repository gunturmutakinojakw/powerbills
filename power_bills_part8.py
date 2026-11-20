# === Stage 8: Фильтрация записей ===
# Project: PowerBills
def filter_by_tariff(records, tariff):
    return [rec for rec in records if rec["tariff"] == tariff]


def filter_by_date_range(records, start_date, end_date):
    return [rec for rec in records if start_date <= rec["period"] <= end_date]


def filter_by_tariff_and_date(records, tariff, start_date, end_date):
    return filter_by_date_range(filter_by_tariff(records, tariff), start_date, end_date)


def filter_records(records, *, tariff=None, start_date=None, end_date=None):
    result = records
    if tariff is not None:
        result = filter_by_tariff(result, tariff)
    if start_date is not None and end_date is not None:
        result = filter_by_date_range(result, start_date, end_date)
    elif start_date is not None:
        result = filter_by_date_range(result, start_date, None)
    elif end_date is not None:
        result = filter_by_date_range(result, None, end_date)
    return result


if __name__ == "__main__":
    sample = [
        {"period": "2024-01", "tariff": "day", "usage": 100, "amount": 1000},
        {"period": "2024-02", "tariff": "night", "usage": 50, "amount": 500},
        {"period": "2024-03", "tariff": "day", "usage": 120, "amount": 1200},
    ]

    print(filter_by_tariff(sample, "day"))
    print(filter_by_tariff_and_date(sample, "day", "2024-01-01", "2024-03-31"))
    print(filter_records(sample, tariff="night", start_date="2024-01-01"))
