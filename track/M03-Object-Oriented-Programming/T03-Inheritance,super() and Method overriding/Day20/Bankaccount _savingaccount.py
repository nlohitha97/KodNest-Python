class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder

    def show_holder(self):
        return f"Account Holder: {self.account_holder}"


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance):
        # Call the parent constructor
        super().__init__(account_holder)

        # Store balance
        self.balance = balance

    def show_balance(self):
        # Return the balance
        return f"Account Balance: {self.balance}"


name = input()
balance = int(input())

account = SavingsAccount(name, balance)

print(account.show_holder())
print(account.show_balance())