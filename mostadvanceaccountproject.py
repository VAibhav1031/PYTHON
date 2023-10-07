class Account:

    def __init__(self, owner, balance, account_type, pin):
        self.owner = owner
        self.balance = balance
        self.account_type = account_type
        self.pin = pin
        self.transaction_history = []

    def deposit(self, deposit_amount):
        if deposit_amount > 0:
            self.balance += deposit_amount
            self.transaction_history.append(f"Deposit: ${deposit_amount}")
            return f"${deposit_amount} Deposit Accepted"
        else:
            return "Invalid deposit amount."

    def withdraw(self, withdrawal_amount):
        if withdrawal_amount > 0:
            if withdrawal_amount <= self.balance:
                self.balance -= withdrawal_amount
                self.transaction_history.append(f"Withdrawal: ${withdrawal_amount}")
                return f"${withdrawal_amount} Withdrawal Accepted"
            else:
                return "Funds Unavailable!"
        else:
            return "Invalid withdrawal amount."

    def get_balance(self):
        return f"Account Balance: ${self.balance}"

    def show_transaction_history(self):
        return "\n".join(self.transaction_history)

    def calculate_interest(self, rate):
        if self.account_type == 'Savings':
            interest = (self.balance * rate) / 100
            self.balance += interest
            self.transaction_history.append(f"Interest Added: ${interest}")
            return f"Interest of ${interest} added to the account."
        else:
            return "Interest calculation is not applicable to this account type."

    def close_account(self):
        self.balance = 0
        self.transaction_history.append("Account Closed")
        return "Account Closed. Remaining balance has been withdrawn."

# Create an account
acct1 = Account('Vaibhav', 4500, 'Savings', '1234')  # Account with a PIN '1234'

print("WELCOME TO TIWARI-BANK ATM!!")
while True:
    pin = input("Enter your PIN: ")
    if pin == acct1.pin:
        print(f"Welcome, {acct1.owner}!")

        while True:
            print("\nSELECT OPTION FOR SERVICES:")
            print("1. Account Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transaction History")
            print("5. Calculate Interest")
            print("6. Close Account")
            print("7. Exit")

            choice_str = input("Enter your choice: ")
            try:
                choice = int(choice_str)
            except ValueError:
                choice = 0

            if choice == 1:
                print(acct1.get_balance())
            elif choice == 2:
                deposit_amount = float(input("Enter the deposit amount: $"))
                print(acct1.deposit(deposit_amount))
            elif choice == 3:
                withdrawal_amount = float(input("Enter the withdrawal amount: $"))
                print(acct1.withdraw(withdrawal_amount))
            elif choice == 4:
                print(acct1.show_transaction_history())
            elif choice == 5:
                interest_rate = float(input("Enter the interest rate (e.g., 5 for 5%): "))
                print(acct1.calculate_interest(interest_rate))
            elif choice == 6:
                confirmation = input("Are you sure you want to close the account? (Y/N): ").lower()
                if confirmation == 'y':
                    print(acct1.close_account())
                    exit()
                else:
                    print("Account closure canceled.")
            elif choice == 7:
                print("Thank you for using TIWARI-BANK ATM! Goodbye.")
                exit()
            else:
                print("INVALID CHOICE")

            # Ask if the user wants to continue
            continue_choice = input("Do you want to perform another transaction? (Y/N): ").lower()
            if continue_choice != 'y':
                break  # Exit the inner loop and return to PIN entry
    else:
        print("Incorrect PIN. Please try again.")
