# === Stage 6: Связанная сущность ===
# Project: PowerBills
billing_payment.py

from datetime import date


class Payment:
    """Платёж по счёту за электроэнергию.

    Связан со счётом через внешний идентификатор billing_id.
    """

    def __init__(self, billing_id, amount, paid_on=None):
        self.billing_id = billing_id
        self.amount = amount
        self.paid_on = paid_on or date.today()

    def __repr__(self):
        return (
            f"Payment(billing_id={self.billing_id}, "
            f"amount={self.amount}, paid_on={self.paid_on})"
        )

    def is_paid(self):
        return self.amount > 0


class PaymentBook:
    """Книга платежей: хранение и работа с платёжами по счётчикам billing_id."""

    def __init__(self):
        self._payments = {}

    def add_payment(self, payment):
        self._payments[payment.billing_id] = payment
        return payment

    def add_payment_raw(self, billing_id, amount, paid_on=None):
        payment = Payment(billing_id, amount, paid_on)
        return self.add_payment(payment)

    def get_payment(self, billing_id):
        return self._payments.get(billing_id)

    def get_payments(self, billing_id):
        return [p for p in self._payments.values() if p.billing_id == billing_id]

    def total_paid(self, billing_id):
        return sum(p.amount for p in self.get_payments(billing_id))

    def list_payments(self):
        return list(self._payments.values())


if __name__ == "__main__":
    book = PaymentBook()
    book.add_payment_raw(42, 1200.5, date(2024, 1, 15))
    book.add_payment_raw(42, 1300.0)
    print(book.get_payments(42))
    print(book.total_paid(42))
