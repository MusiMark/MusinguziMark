class BankAccount:
    def __init__(self):
        self.__balance= 1000000

    def deposit(self,amount):
        self.__balance += amount

    def show_balance(self):
        print(self.__balance)


acc = BankAccount()
acc.deposit(100000)
acc.show_balance()


#Exercise 2

class MobileMoney:
    def __init__(self):
        self.__balance= 0

    def deposit(self,amount):
        self.__balance += amount

    def withdraw(self,amount):
        self.__balance -= amount

    def show_balance(self):
        print(f"Current Balance: {self.__balance}")


account1 = MobileMoney()
account1.deposit(100000)
account1.show_balance()
account1.withdraw(20000)
account1.show_balance()