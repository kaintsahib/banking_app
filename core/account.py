from typing import List
from datetime import datetime


class InsufficientFundsError(Exception):
    pass


class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self._owner = owner
        self._balance = balance
        self._transactions: List[str] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount
        self._transactions.append(
            f"{datetime.now()} - Deposited {amount}"
        )

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise InsufficientFundsError("Not enough balance")

        self._balance -= amount
        self._transactions.append(
            f"{datetime.now()} - Withdrawn {amount}"
        )

    def get_transactions(self) -> List[str]:
        return self._transactions

    def __repr__(self) -> str:
        return f"Account(owner={self._owner}, balance={self._balance})"
