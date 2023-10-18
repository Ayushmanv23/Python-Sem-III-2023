#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ayush
#
# Created:     29-09-2023
# Copyright:   (c) ayush 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Atm machine basic op.
Balance = 20000000000
while True:
    print("Welcome to our ATM:")
    print("1. Check account Balance")
    print("2. Withdraw Money from account")
    print("3. Deposit Money")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        print(f"Your account balance is ${Balance}")
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount. Please enter a valid amount.")
        elif amount > Balance:
            print("Insufficient amount.")
        else:
            Balance -= amount
            print(f"Withdrew ${amount}. Your new balance is ${Balance}")
    elif choice == '3':
        amount = float(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid amount. Please enter a valid amount.")
        else:
            Balance += amount
            print(f"Deposited ${amount}. Your new balance is ${Balance}")
    elif choice == '4':
        print("Thank you for using our ATM.+")
        break
    else:
        print("Invalid choice. Please choose a valid option (1/2/3/4).")