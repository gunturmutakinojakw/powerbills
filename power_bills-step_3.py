# === Stage 3: Хранилище в памяти ===
# Project: PowerBills
memory_store.py

from typing import Dict, List, Type, TypeVar, Generic, Optional, Any


T = TypeVar("T")


class MemoryStore(Generic[T]):
    """Простое хранилище в памяти с поддержкой добавления,
    получения по идентификатору и получения списка записей."""

    def __init__(self) -> None:
        self._items: Dict[Any, T] = {}

    def add(self, record: T, identifier: Any) -> T:
        self._items[identifier] = record
        return record

    def get(self, identifier: Any) -> Optional[T]:
        return self._items.get(identifier)

    def all(self) -> List[T]:
        return list(self._items.values())

    def __len__(self) -> int:
        return len(self._items)


class AccountStore(MemoryStore):
    """Специализированное хранилище для счётов за электричество."""

    def __init__(self) -> None:
        super().__init__()
        self._sequence: int = 0

    def add(self, account: T, identifier: Optional[Any] = None) -> T:
        if identifier is None:
            self._sequence += 1
            identifier = self._sequence
        return super().add(account, identifier)

    def get(self, identifier: Any) -> Optional[T]:
        return self._items.get(identifier)

    def all(self) -> List[T]:
        return list(self._items.values())

    def __len__(self) -> int:
        return len(self._items)


def build_account_store() -> AccountStore:
    return AccountStore()


if __name__ == "__main__":
    store = build_account_store()
    print(len(store))
    print(store.add({"period": "2024-01", "tariff": 5.0, "usage": 100, "amount": 500}))
    print(store.get(1))
    print(store.all())
