class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited: $" + str(amount) + ". New balance: $" + str(self.balance))

    def withdraw(self, amount, pin):
        if pin == self.pin:
            if amount <= self.balance:
                self.balance -= amount
                print("Withdrew: $" + str(amount) + ". New balance: $" + str(self.balance))
            else:
                print("Insufficient funds. Current balance: $" + str(self.balance))
        else:
            print("Incorrect PIN. Transaction denied.")
            
    def display_balance(self, pin):
        if pin == self.pin:
            print("Current balance: $" + str(self.balance))
        else:
            print("Incorrect PIN. Cannot display balance.") 

account1 = BankAccount("Claudia", "Chavez", 1, "Checking", 1234, 1000)
account2 = BankAccount("Saul", "Jaguar", 22, "Savings", 1234, 5000)
account3 = BankAccount("Jesus", "Castellanos", 333, "Checking", 1234, 2500)

def welcome():
    
    print("\nWelcome to the favorite bank in the world")
    
    id = int(input("\nPlease enter your account ID: "))
    if id == account1.account_id:
        print("\nWelcome Karina Chavez")
        pin1 = int(input("\nPlease enter your PIN: "))
        account1.display_balance(pin1)
        opc = int(input("\nWould you like to make a deposit or withdrawal? (1 for deposit, 2 for withdrawal): "))
        if opc == 1:
            amount = float(input("\nEnter amount to deposit: $"))
            account1.deposit(amount)
        elif opc == 2:
            amount = float(input("\nEnter amount to withdraw: $"))
            pin2 = int(input("\nPlease enter your PIN again for withdrawal: "))
            account1.withdraw(amount, pin2)
        else:
            print("Invalid option.")
    elif id == account2.account_id:
        print("\nWelcome Mario Castellanos")
        pin1 = int(input("\nPlease enter your PIN: "))
        account2.display_balance(pin1)
        opc = int(input("\nWould you like to make a deposit or withdrawal? (1 for deposit, 2 for withdrawal): "))
        if opc == 1:
            amount = float(input("\nEnter amount to deposit: $"))
            account2.deposit(amount)
        elif opc == 2:
            amount = float(input("\nEnter amount to withdraw: $"))
            pin2 = int(input("\nPlease enter your PIN again for withdrawal: "))
            account2.withdraw(amount, pin2)
        else:
            print("Invalid option.")
    elif id == account3.account_id:
        print("\nWelcome Jesus Castellanos")
        pin1 = int(input("\nPlease enter your PIN: "))
        account3.display_balance(pin1)
        opc = int(input("\nWould you like to make a deposit or withdrawal? (1 for deposit, 2 for withdrawal): "))
        if opc == 1:
            amount = float(input("\nEnter amount to deposit: $"))
            account3.deposit(amount)
        elif opc == 2:
            amount = float(input("\nEnter amount to withdraw: $"))
            pin2 = int(input("\nPlease enter your PIN again for withdrawal: "))
            account3.withdraw(amount, pin2)
    else:
        print("Account not found.")

welcome()