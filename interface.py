class Account:
    def __init__(self, user_id, pin, balance=0):
        self.user_id = user_id
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds!")

    def transfer(self, recipient, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.user_id}")
        else:
            print("Insufficient funds!")

    def get_transaction_history(self):
        return self.transaction_history

class ATM:
    def __init__(self, accounts):
        self.accounts = accounts

    def login(self, user_id, pin):
        for account in self.accounts:
            if account.user_id == user_id and account.pin == pin:
                return account
        return None

    def start(self):
        while True:
            user_id = input("Enter user ID: ")
            pin = input("Enter PIN: ")
            account = self.login(user_id, pin)
            if account:
                print("Login successful!")
                self.atm_menu(account)
            else:
                print("Invalid user ID or PIN. Please try again.")

    def atm_menu(self, account):
        while True:
            print("\nATM Menu:")
            print("1. View Transactions History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")
            choice = input("Enter choice: ")

            if choice == '1':
                print("Transaction History:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            elif choice == '4':
                recipient_id = input("Enter recipient's user ID: ")
                recipient = self.get_account_by_id(recipient_id)
                if recipient:
                    amount = float(input("Enter amount to transfer: "))
                    account.transfer(recipient, amount)
                else:
                    print("Recipient not found.")
            elif choice == '5':
                print("Thank you for using our ATM. Goodbye!")
                return
            else:
                print("Invalid choice. Please try again.")

    def get_account_by_id(self, user_id):
        for account in self.accounts:
            if account.user_id == user_id:
                return account
        return None

# Example usage:
if __name__ == "__main__":
    # Create some accounts
    accounts = [Account("user1", "1234"), Account("user2", "5678")]

    # Initialize ATM with the accounts
    atm = ATM(accounts)

    # Start the ATM
    atm.start()


