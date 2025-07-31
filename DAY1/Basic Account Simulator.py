# Basic Account Simulator

balance = 0  # Initial account balance

def show_menu():
    print("\n Account Simulator Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        print(f"Your current balance is: Rs. {balance}")
    
    elif choice == '2':
        amount = float(input("Enter amount to deposit: Rs. "))
        if amount > 0:
            balance += amount
            print(f"Deposited Rs. {amount}. New balance: Rs. {balance}")
        else:
            print("Invalid deposit amount.")
    
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: Rs. "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrawn Rs. {amount}. Remaining balance: Rs. {balance}")
        else:
            print("Insufficient funds or invalid amount.")
    
    elif choice == '4':
        print("Exiting... Thank you for using the simulator.")
        break

    else:
        print("Invalid option. Please choose from 1 to 4.")