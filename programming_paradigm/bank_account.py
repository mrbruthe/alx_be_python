# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance."""
        self.__balance = initial_balance  # private variable for encapsulation

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        """Withdraw an amount from the account if funds are sufficient."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True
        print("Insufficient funds.")
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__balance:.1f}")

    def get_balance(self):
        """Return the current balance (for internal use or testing)."""
        return self.__balance
