# === Stage 2: Проверка полей ===
# Project: PowerBills
from datetime import datetime, timedelta


def parse_period(raw: str) -> tuple[str, str] | None:
    """Нормализует строку периода вида '2024-01' в (год, месяц) с валидацией."""
    if raw is None:
        return None
    raw = raw.strip()
    try:
        date = datetime.strptime(raw, "%Y-%m")
    except ValueError:
        return None
    return date.strftime("%Y"), date.strftime("%m")


def parse_tariff(raw: str) -> str:
    """Нормализует тариф, приводя его к верхнему регистру и убирая пробелы."""
    if raw is None:
        raise ValueError("Тариф не может быть пустым")
    return str(raw).strip().upper()


def parse_consumption(raw: str) -> float | None:
    """Нормализует расход электроэнергии в киловатт-часах."""
    if raw is None:
        return None
    try:
        value = float(str(raw).strip())
    except ValueError:
        return None
    if value < 0:
        raise ValueError("Расход не может быть отрицательным")
    return value


def parse_amount(raw: str) -> float | None:
    """Нормализует сумму к оплате в рублях."""
    if raw is None:
        return None
    try:
        value = float(str(raw).strip())
    except ValueError:
        return None
    if value < 0:
        raise ValueError("Сумма не может быть отрицательной")
    return round(value, 2)


def validate_bill(period: str | None, tariff: str | None,
                  consumption: str | None, amount: str | None) -> list[str]:
    """Возвращает список понятных сообщений об ошибках для полей счёта."""
    errors: list[str] = []

    if period is not None:
        parsed = parse_period(period)
        if parsed is None:
            errors.append("Неверный формат периода: ожидается 'ГГГГ-ММ', например '2024-01'")

    if tariff is not None:
        try:
            parse_tariff(tariff)
        except ValueError as exc:
            errors.append(str(exc))

    if consumption is not None:
        try:
            parse_consumption(consumption)
        except ValueError as exc:
            errors.append(str(exc))

    if amount is not None:
        try:
            parse_amount(amount)
        except ValueError as exc:
            errors.append(str(exc))

    return errors


def normalize_input(period: str | None, tariff: str | None,
                    consumption: str | None, amount: str | None) -> dict:
    """Нормализует и валидирует все поля счёта, возвращая чистые значения."""
    clean = {
        "period": parse_period(period),
        "tariff": parse_tariff(tariff),
        "consumption": parse_consumption(consumption),
        "amount": parse_amount(amount),
    }
    errors = validate_bill(period, tariff, consumption, amount)
    if errors:
        clean["_errors"] = errors
    return clean


if __name__ == "__main__":
    sample = normalize_input(
        period="2024-13",
        tariff="Дневной Тариф",
        consumption="150",
        amount="-100",
    )
    if sample.get("_errors"):
        for message in sample["_errors"]:
            print("Ошибка:", message)
    else:
        print("Счёт валиден:", sample)
