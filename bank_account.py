class BankAccount:
    def __init__(self, account_holder, initial_balance=100):
        self.account_holder = account_holder
        self.__balance = initial_balance  # private for encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__balance}")

    def get_balance(self):
        return self.__balance
