class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        """Increase balance by given amount"""
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount if sufficient balance is available"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient balance")

    def display_balance(self):
        """Display account details"""
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Type: {self.account_type}")
        print(f"Current Balance: {self.balance}\n")


if __name__ == "__main__":
    # Create two bank accounts
    account1 = BankAccount("Alice", 1000.0, "Savings")
    account2 = BankAccount("Bob", 500.0, "Current")

    # Perform operations on account1
    print("---- Account 1 Operations ----")
    account1.display_balance()
    account1.deposit(500)
    account1.withdraw(300)
    account1.withdraw(1500)  # should show insufficient
    account1.display_balance()

    # Perform operations on account2
    print("---- Account 2 Operations ----")
    account2.display_balance()
    account2.deposit(200)
    account2.withdraw(100)
    account2.display_balance()
