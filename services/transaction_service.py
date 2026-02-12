from core.account import Account


class TransactionService:
    def transfer(self, sender: Account, receiver: Account, amount: float) -> None:
        sender.withdraw(amount)
        receiver.deposit(amount)
