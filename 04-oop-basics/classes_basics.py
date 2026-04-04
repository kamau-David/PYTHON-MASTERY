"""Class definitions, instances, and instance methods."""

class BankAccount:
    """A simple bank account with a balance and basic operations."""

    # Class variable - shared across ALL instances
    bank_name = "Meru Community Bank"

    def __init__(self, owner: str, balance: float = 0.0):
        # Instance variables - unique per object
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def describe(self) -> str:
        return f"{self.owner}'s account at {self.bank_name}: KES {self.balance:.2f}"


account = BankAccount("Davian", 1000)
account.deposit(500)
account.withdraw(200)
print(account.describe())

second_account = BankAccount("Amina")
print(second_account.describe())
print(BankAccount.bank_name)   # class variable accessible without an instance
