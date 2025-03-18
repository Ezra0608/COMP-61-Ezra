initial_balance = 1000.00
current_balance = initial_balance
print("Welcome to Simple ATM simulator")
print("Your current balance is: ",f'${initial_balance:.2f}')
print("menu")
print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")

while True:
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        print("Your current balance is: ",f'${current_balance:.2f}')
    elif(choice == 2):
        deposit_amount = float(input("Enter the amount to deposit: $"))
        current_balance += deposit_amount
        print("Deposit successful! Your new balance is: ",f'${current_balance:.2f}')
    elif(choice == 3):
        withdraw_amount = float(input("Enter the amount to withdraw: $"))
        current_balance -= withdraw_amount
        print("Withdraw successful! Your new balance is: ",f'${current_balance:.2f}')
        
        if withdraw_amount > current_balance:
            print("Insufficient funds!")
    
    else:
        print("Thank you for using the ATM. Goodbye!")
        break
   