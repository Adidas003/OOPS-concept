class ATM:
    def __init__(self, account_type, balance=0, pin=1234):
        self.account_type = account_type
        self.balance = balance
        self.pin = pin

    def validate_pin(self):
        attempts = 3
        while attempts > 0:
            try:
                entered_pin = int(input("Enter your 4-digit PIN: "))
            except ValueError:
                print("Invalid input. Please enter a 4-digit number.")
                continue

            if entered_pin == self.pin:
                print("PIN validated successfully.")
                return True
            else:
                attempts -= 1
                print(f"Incorrect PIN. {attempts} attempts left.")
        
        print("Too many incorrect attempts. Access denied.")
        return False

    def check_balance(self):
        print(f"Your {self.account_type} account balance is: ${self.balance}")
        self.continue_or_exit()

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}.")
            self.check_balance()
        else:
            print("Invalid amount. Please enter a positive value.")
            self.continue_or_exit()

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount}.")
                self.check_balance()
            else:
                print("Insufficient funds.")
                self.continue_or_exit()
        else:
            print("Invalid amount. Please enter a positive value.")
            self.continue_or_exit()
    
    def continue_or_exit(self):
        while True:
            choice = input("Do you want to continue? (y/n): ").lower()
            if choice == 'y':
                return  # Continue to the main menu
            elif choice == 'n':
                print(f"Thank you for using the ATM. Goodbye from your {self.account_type} account!")
                exit()  # Exit the process
            else:
                print("Invalid input. Please enter 'y' to continue or 'n' to exit.")
    
    def run(self):
        if not self.validate_pin():
            return
        
        while True:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == 1:
                self.check_balance()
            elif choice == 2:
                amount = float(input("Enter the amount to deposit: "))
                self.deposit(amount)
            elif choice == 3:
                amount = float(input("Enter the amount to withdraw: "))
                self.withdraw(amount)
            elif choice == 4:
                print(f"Thank you for using the ATM. Goodbye from your {self.account_type} account!")
                break
            else:
                print("Invalid option. Please choose again.")


def initialize_atm():
    while True:
        print("Select Account Type:")
        print("1. Savings")
        print("2. Current")

        account_choice = input("Enter 1 for Savings or 2 for Current: ")
        
        if account_choice == "1":
            account_type = "Savings"
            break
        elif account_choice == "2":
            account_type = "Current"
            break
        else:
            print("Invalid input. Please enter 1 or 2 to select an account type.")

    try:
        pin = int(input("Set a 4-digit PIN for the ATM account: "))
        if not (1000 <= pin <= 9999):
            raise ValueError
    except ValueError:
        print("Invalid input. Setting default PIN to 1234.")
        pin = 1234

    return ATM(account_type=account_type, pin=pin)


atm = initialize_atm()
atm.run()
