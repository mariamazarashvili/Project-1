# create a class for ATM
class ATM:
    def __init__(self, pin_code, account_owner, balance):
        self.pin_code = pin_code
        self.account_owner = account_owner
        self.balance = balance

# Method to check account balance
    def check_balance(self):
        print(f"Account balance for {self.account_owner}: {self.balance} GEL.")


#  Method to deposit money into the account
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} GEL. New balance is {self.balance} GEL.")
        else:
            print(" Amount must be greater than zero.")

# Method to withdraw money from the account
    def withdraw(self, amount):
         if amount < self.balance:
            self.balance -= amount
            print(f"withdraw {amount} GEL. New balance is {self.balance} GEL.")
         else:
            print(f"Withdrawal failed. There is not enough money in the account {self.balance} GEL.")

    def save_to_file(self):
        with open("ATM.txt", "a")as file:
            file.write(f"pin_code:  {self.pin_code}\n")
            file.write(f"account_owner: {self.account_owner}\n")
            file.write(f"balance: {self.balance}\n")
            print(f"Account information saved to {"ATM.txt"}")

# Create an ATM account
account_1 = ATM("1234", "M.A", 1000)
account_2 = ATM("2234", "K.A", 500)

# Perform transactions
account_1.deposit(50)
account_1.withdraw(200)
account_1.check_balance()

account_2.deposit(20)
account_2.withdraw(1000)
account_2.check_balance()

# Save account information to file
account_1.save_to_file()
account_2.save_to_file()





