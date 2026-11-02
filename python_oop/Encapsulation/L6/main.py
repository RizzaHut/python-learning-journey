class BankAccount:
    def __init__(self, account_number: str, initial_balance: float) -> None:
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self) -> str:
        return str(self.__account_number)

    def get_balance(self) -> float:
        return float(self.__balance)

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        self.__balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        elif amount > self.__balance:
            raise ValueError("insufficient funds")
        self.__balance -= amount
