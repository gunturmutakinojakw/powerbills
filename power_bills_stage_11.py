# === Stage 11: Поиск по нескольким словам ===
# Project: PowerBills
def find_accounts(accounts, terms):
    """
    Поиск счетов по нескольким словам с поддержкой исключений.

    terms — список ключевых слов. Счёт считается найденным, если
    хотя бы одно из включённых слов встречается в его строковом
    представлении, и при этом ни одно исключительное слово (начинается
    с «-») в нём не встречается.

    Примеры:
        find_accounts([a, b])                       -> a и b должны совпасть
        find_accounts([a, b, -c])                   -> есть a/b, но не c
        find_accounts(['ab', -a])                   -> «ab» не совпадает с «a»
    """
    keywords = [t for t in terms if not t.startswith('-')]
    exclusions = [t[1:] for t in terms if t.startswith('-')]

    def matches(account):
        text = str(account)
        if any(keyword in text for keyword in keywords):
            if not any(exclusion in text for exclusion in exclusions):
                return True
        return False

    return [account for account in accounts if matches(account)]


if __name__ == '__main__':
    sample = [
        {'period': '2024-01', 'tariff': 'day', 'usage': 100, 'payment': 50},
        {'period': '2024-02', 'tariff': 'night', 'usage': 150, 'payment': 75},
        {'period': '2024-03', 'tariff': 'day', 'usage': 120, 'payment': 60},
    ]

    print(find_accounts(sample, ['2024-01']))
    print(find_accounts(sample, ['day', -'night']))
    print(find_accounts(sample, ['payment']))
