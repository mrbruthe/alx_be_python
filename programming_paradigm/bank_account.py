class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Deposit a positive amount to the account."""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance exists."""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__balance:.2f}")

    def get_balance(self):
        """Return the current balance (for external access)."""
        return self.__balance
