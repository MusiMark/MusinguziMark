# Lab Activity 1
class Transaction:
    def __init__(self, employee_name, balance):
        self.employee_name = employee_name
        self.balance = balance

    def process(self):
        print("Processing transaction...")


# Child Class - Deposit
class Deposit(Transaction):

    # Simulated Method Overloading using default arguments
    def deposit(self, amount, bonus=0):
        self.balance += (amount + bonus)
        print(f"{self.employee_name} deposited {amount}")
        if bonus > 0:
            print(f"Bonus added: {bonus}")
        print(f"New Balance: {self.balance}")

    # Method Overriding
    def process(self):
        print("Deposit transaction processed.")


# Child Class - Withdrawal
class Withdrawal(Transaction):

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.employee_name} withdrew {amount}")
            print(f"New Balance: {self.balance}")
        else:
            print("Insufficient funds!")

    # Method Overriding
    def process(self):
        print("Withdrawal transaction processed.")


# Child Class - Transfer
class Transfer(Transaction):

    def transfer(self, amount, receiver):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.employee_name} transferred {amount} to {receiver}")
            print(f"Remaining Balance: {self.balance}")
        else:
            print("Insufficient funds for transfer!")

    # Method Overriding
    def process(self):
        print("Transfer transaction processed.")


# Demonstration
print("=== Employee Banking System ===")

# Deposit
emp_deposit = Deposit("John", 5000)
emp_deposit.process()
emp_deposit.deposit(2000)           # Normal deposit
emp_deposit.deposit(1000, 200)      # Overloaded version with bonus

print()

# Withdrawal
emp_withdraw = Withdrawal("John", emp_deposit.balance)
emp_withdraw.process()
emp_withdraw.withdraw(1500)

print()

# Transfer
emp_transfer = Transfer("John", emp_withdraw.balance)
emp_transfer.process()
emp_transfer.transfer(1000, "Mary")