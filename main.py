from services import *

while True:
    print("\n1. Balance\n2. Deposit\n3. Withdraw\n4. Statement\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print(check_balance())

    elif choice == "2":
        amt = int(input("Amount: "))
        deposit(amt)

    elif choice == "3":
        amt = int(input("Amount: "))
        if not withdraw(amt):
            print("Insufficient balance")

    elif choice == "4":
        for t in get_statement():
            print(t)

    elif choice == "5":
        break