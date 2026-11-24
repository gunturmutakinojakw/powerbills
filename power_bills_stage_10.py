# === Stage 10: Текстовый поиск ===
# Project: PowerBills
def search_in_fields(records, query):
    query = query.lower().strip()
    matches = []
    for record in records:
        haystack = " ".join(str(value).lower() for value in record.values())
        if query in haystack:
            matches.append(record)
    return matches


def highlight_line(line, query):
    if not query:
        return line
    result = list(line)
    query_len = len(query)
    start = 0
    while True:
        index = line.find(query, start)
        if index == -1:
            break
        for position in range(index, index + query_len):
            if 0 <= position < len(result):
                result[position] = '\033[1;33m' + result[position] + '\033[0m'
        start = index + 1
    return "".join(result)


def find_by_text(records, field_values, query):
    query = query.lower().strip()
    matches = []
    for record in records:
        haystack = " ".join(str(value).lower() for value in field_values)
        if query in haystack:
            matches.append(record)
    return matches


def display_search_results(records, field_values, query):
    query = query.lower().strip()
    matches = find_by_text(records, field_values, query)
    if not matches:
        print("Ничего не найдено")
        return
    print(f"Найдено совпадений: {len(matches)}")
    for record in matches:
        line = "  ".join(str(value) for value in record.values())
        print(highlight_line(line, query))


if __name__ == "__main__":
    sample_records = [
        {"id": 1, "period": "2024-01", "tariff": "дневной", "usage": 120, "amount": 480},
        {"id": 2, "period": "2024-02", "tariff": "ночной", "usage": 80, "amount": 320},
        {"id": 3, "period": "2024-03", "tariff": "дневной", "usage": 150, "amount": 600},
    ]
    search_query = "ДНЕВНОЙ"
    display_search_results(sample_records, ["period", "tariff", "usage", "amount"], search_query)
