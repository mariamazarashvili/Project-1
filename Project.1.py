# create a class for Cardholder
class Cardholder:
    def __init__(self, account_number, pin, account_owner, balance):
        self.account_number = account_number
        self.pin = pin
        self.account_owner = account_owner
        self.balance = balance

    # Method to check account balance
    def check_balance(self):
        print(f"Account balance for {self.account_owner}: {self.balance} .")

    #  Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" {self.account_owner},your new balance is: {self.balance}.GEL")
        else:
            print(" Amount must be greater than zero.")

    # Method to withdraw money from the account
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.account_owner},your new balance is: {self.balance}.GEL")
        else:
            print(f"Withdraw failed. There is not enough money in the account {self.balance}.GEL")

        # Method to save to file
    def save_to_file(self):
        with open("Atm.txt", "w") as file:
            file.writeline(f"account_number:  {self.account_number}\n")
            file.write(f"pin: {self.pin}\n")
            file.write(f"account_owner:   {self.account_owner}\n")
            file.write(f"balance: {self.balance}\n")
            file.write("\n")  # Add newline to separate entries
            print("Information saved to 'Atm.txt'")

# Method to run the user interface
def user_menu(user):
    while True:
        print("\nMenu:")
        print("1. Show  balance")
        print("2. Deposit  ")
        print("3. Withdraw  ")
        print("4. Exit ")

        choice = input("Enter your choice (1-4):")
        if choice == '1':
            print(user.account_owner,", your balance is:", user.balance, "GEL")
        elif choice == '2':
            deposit_amount = float(input("How much money do you want to deposit: "))
            user.deposit(deposit_amount)
        elif choice == '3':
            withdraw_amount = float(input("How much money do you want to withdraw:"))
            user.withdraw(withdraw_amount)
        elif choice == '4':
            print("Exiting the program...")
            exit()
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
def check_pin(user_list):
    attempts = 3  # Number of attempts allowed
    while attempts > 0:
        try:
            user_pin = int(input("Enter your PIN: "))
        except ValueError:
            print("PIN cannot be empty.")
            continue
        else:
            for key in user_list:
                if key.pin == user_pin:
                    user_menu(key)
                    return
            else:
                print("Invalid PIN. Please try again!")
                attempts -= 1
    print("Maximum attempts reached. Exiting...")
    exit()


# create holders account list
list_of_cardholders = [Cardholder("1234455",  1234, "Mariam", 0),
                       Cardholder("5678900", 2345, "Ilia", 1000),
                       Cardholder("2344553", 5678, "Nino", 3000)]


check_pin(list_of_cardholders)
for cardholder in list_of_cardholders:
    cardholder.save_to_file()
