# === Stage 4: Редактирование записей ===
# Project: PowerBills
def edit_bill(bills, bill_id, changes):
    """Редактирует сущность «счёт» по идентификатору билла.

    Проверка: меняются только допустимые поля, идентификатор существует,
    и значения после изменения остаются валидными. Возвращает обновлённый
    счёт или None, если изменения нельзя применить.
    """
    DOABLE_FIELDS = {"period", "tariff", "consumption", "amount"}
    VALID_PERIODS = {"daily", "weekly", "monthly"}
    VALID_TARIFFS = {"standard", "night", "peak", "green"}

    if not isinstance(changes, dict):
        return None
    if not DOABLE_FIELDS.issuperset(changes.keys()):
        return None
    bill = next((b for b in bills if b.get("id") == bill_id), None)
    if bill is None:
        return None

    updated = dict(bill)
    for field, value in changes.items():
        if field == "period":
            if value not in VALID_PERIODS:
                return None
            updated["period"] = value
        elif field == "tariff":
            if value not in VALID_TARIFFS:
                return None
            updated["tariff"] = value
        elif field == "consumption":
            if not isinstance(value, (int, float)) or value <= 0:
                return None
            updated["consumption"] = value
        elif field == "amount":
            if not isinstance(value, (int, float)) or value < 0:
                return None
            updated["amount"] = value

    if updated["consumption"] <= 0 and updated["amount"] > 0:
        return None

    return updated


def recalculate_amount(tariff, consumption):
    """Вычисляет сумму по тарифу и расходу (вспомогательная функция)."""
    multipliers = {
        "standard": 1.0,
        "night": 0.6,
        "peak": 1.5,
        "green": 0.8,
    }
    if tariff not in multipliers:
        return None
    return round(consumption * multipliers[tariff], 2)
