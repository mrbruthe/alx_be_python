# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # private for encapsulation

    def deposit(self, amount):
        """Add amount to balance. Returns True if successful."""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Subtract amount from balance if funds are sufficient. Returns True if successful."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        """Return current balance."""
        return self.__balance

    def display_balance(self):
        """Print the current balance formatted to 2 decimal places."""
        print(f"Current Balance: ${self.__balance:.2f}")
