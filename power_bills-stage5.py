# === Stage 5: Удаление и восстановление ===
# Project: PowerBills
import copy
from datetime import datetime
from typing import Optional


class SoftDeleteError(KeyError):
    """Ошибка при удалении несуществующего счёта."""


class PowerBill:
    """Счёт за электроэнергию с поддержкой мягкого удаления."""

    def __init__(self, period: str, tariff: str, consumption: float, amount: float):
        self.period = period
        self.tariff = tariff
        self.consumption = consumption
        self.amount = amount
        self.is_deleted = False
        self.deleted_at: Optional[datetime] = None
        self.deleted_by: Optional[str] = None

    def soft_delete(self, user: str) -> None:
        """Мягкое удаление: помечаем счёт как удалённый, но сохраняем данные."""
        if self.is_deleted:
            raise SoftDeleteError(f"Счёт {self.period} уже удалён")
        self.is_deleted = True
        self.deleted_at = datetime.now()
        self.deleted_by = user

    def restore(self) -> None:
        """Восстанавливает удалённый счёт."""
        if not self.is_deleted:
            raise SoftDeleteError(f"Счёт {self.period} не был удалён")
        self.is_deleted = False
        self.deleted_at = None
        self.deleted_by = None


class PowerBillRegistry:
    """Регистр счётов с поддержкой мягкого удаления и восстановления."""

    def __init__(self):
        self._bills: list[PowerBill] = []
        self._deleted_bills: list[PowerBill] = []

    def add(self, bill: PowerBill) -> PowerBill:
        self._bills.append(bill)
        return bill

    def get(self, period: str) -> Optional[PowerBill]:
        for bill in self._bills:
            if bill.period == period:
                return bill
        return None

    def delete(self, period: str) -> None:
        """Мягкое удаление счёта. Данные сохраняются и могут быть восстановлены."""
        bill = self.get(period)
        if bill is None:
            raise SoftDeleteError(f"Счёт за период {period} не найден")
        bill.soft_delete(user="system")
        self._deleted_bills.append(copy.deepcopy(bill))

    def restore(self, period: str) -> None:
        """Восстанавливает ранее удалённый счёт."""
        bill = self.get(period)
        if bill is not None and bill.is_deleted:
            bill.restore()
        else:
            raise SoftDeleteError(f"Счёт за период {period} не был удалён")

    def get_deleted(self, period: str) -> Optional[PowerBill]:
        for bill in self._deleted_bills:
            if bill.period == period:
                return bill
        return None
