import json
import os

DATA_FILE = "data.json"

# Load data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

class BankAccount:
    def __init__(self, username):
        self.username = username
        self.data = load_data()

    def create_account(self, password):
        if self.username in self.data:
            print("Account already exists!")
            return

        self.data[self.username] = {
            "password": password,
            "balance": 0,
            "transactions": []
        }
        save_data(self.data)
        print("Account created successfully!")

    def login(self, password):
        if self.username in self.data and self.data[self.username]["password"] == password:
            print("Login successful!")
            return True
        print("Invalid credentials!")
        return False

    def deposit(self, amount):
        self.data[self.username]["balance"] += amount
        self.data[self.username]["transactions"].append(f"Deposited {amount}")
        save_data(self.data)
        print(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.data[self.username]["balance"] >= amount:
            self.data[self.username]["balance"] -= amount
            self.data[self.username]["transactions"].append(f"Withdrew {amount}")
            save_data(self.data)
            print(f"Withdrew {amount}")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Balance:", self.data[self.username]["balance"])

    def transaction_history(self):
        print("Transactions:")
        for t in self.data[self.username]["transactions"]:
            print("-", t)


def main():
    print("=== Smart Banking System ===")
    username = input("Enter username: ")
    account = BankAccount(username)

    choice = input("1. Create Account\n2. Login\nChoose: ")

    if choice == "1":
        password = input("Create password: ")
        account.create_account(password)

    elif choice == "2":
        password = input("Enter password: ")
        if account.login(password):
            while True:
                print("\n1. Deposit\n2. Withdraw\n3. Balance\n4. Transactions\n5. Exit")
                opt = input("Choose: ")

                if opt == "1":
                    amt = float(input("Enter amount: "))
                    account.deposit(amt)

                elif opt == "2":
                    amt = float(input("Enter amount: "))
                    account.withdraw(amt)

                elif opt == "3":
                    account.check_balance()

                elif opt == "4":
                    account.transaction_history()

                elif opt == "5":
                    break

                else:
                    print("Invalid option!")

if __name__ == "__main__":
    main()