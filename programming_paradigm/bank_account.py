class BankAccount:
    def __init__(self, initial_balance=0):
        # Initialize the account balance as a float
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.account_balance += float(amount)

    def withdraw(self, amount):
        """Deduct the amount from the account balance if sufficient funds exist.
        Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= float(amount)
            return True
        return False

    def display_balance(self):
        """Print the current balance in a user-friendly float format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
