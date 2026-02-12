from core.account import Account
from services.transaction_service import TransactionService

def main() -> None:
    acc1 = Account("Gaurav", 1000)
    acc2 = Account("Investor", 500)

    service = TransactionService()
    service.transfer(acc1, acc2, 300)

    print(acc1)
    print(acc2)

if __name__ == "__main__":
    main()
