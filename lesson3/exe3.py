print("BANKING SYSTEM".center(30,"~"))

balance = 1000

while balance > 0:
    print(f"Current Balance: {balance}")
    choice = int(input("1) Deposit\n2) Withdraw\n3) Exit\n Enter(1,2 or 3): "))
    if choice == 1:
        amount = int(input("Enter amount you want to deposit: "))
        balance += amount
        print(f"Deposited: {amount}")
    elif choice == 2:
        if balance <= 0:
            print("Insufficient balance")
        else:
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds")
            else:
                balance -= amount
                print(f"Withdrawing: {amount}")

    elif choice == 3:
        break
    else:
        print("Invalid choice")

