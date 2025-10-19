class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # <-- use __balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:  # <-- check __balance
            self.__balance -= amount      # <-- subtract from __balance
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.__balance:.2f}")

    def get_balance(self):
        return self.__balance
