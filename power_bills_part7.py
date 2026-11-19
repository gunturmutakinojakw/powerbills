# === Stage 7: Генерация идентификаторов ===
# Project: PowerBills
import string
import secrets


PROJECT_PREFIX = "PB"


def _is_reserved(identifier: str) -> bool:
    return identifier in ("True", "False", "None") or identifier[0].isdigit()


def _make_unique(base: str, used: set, attempts: int = 100) -> str:
    candidate = base
    for i in range(1, attempts + 1):
        if candidate not in used:
            return candidate
        candidate = f"{base}-{i}"
    raise ValueError(f"Не удалось подобрать уникальный id среди {attempts} вариантов: {base}")


def generate_id(kind: str, used: set | None = None) -> str:
    used = used if used is not None else set()
    prefix = f"{PROJECT_PREFIX}-{kind}"
    alphabet = string.ascii_lowercase + string.digits
    while True:
        random_part = "".join(secrets.choice(alphabet) for _ in range(8))
        candidate = f"{prefix}-{random_part}"
        if candidate not in used and not _is_reserved(candidate):
            used.add(candidate)
            return candidate
        used.discard(candidate)


def generate_id_from_string(base: str, used: set | None = None) -> str:
    used = used if used is not None else set()
    return _make_unique(base, used)
