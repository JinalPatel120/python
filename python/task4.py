import datetime

class Account:
    def __init__(self, name: str, pin: str, balance: float):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, pin: str) -> bool:
        return self.pin == pin

    def update_balance(self, amount: float):
        ''' you will update your balance or deposit amount'''
        self.balance += amount

    def add_transaction(self, transaction_type: str, amount: float):
        ''' this function gives summary of transaction with amount and date '''
        self.transaction_history.append({
            'type': transaction_type,
            'amount': amount,
            'date': datetime.datetime.now()
        })

    def update_name(self, new_name: str):
        ''' you will update name in your account'''
        self.name = new_name

    def update_pin(self, new_pin: str):
        ''' you will update pin in your account'''
        self.pin = new_pin


class ATM:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1

    def create_account(self, name: str, pin: str, initial_balance: float) -> int:
        ''' Account was created with valid name, pin and balance else will raise error'''
        if not isinstance(name, str) or not name.isalpha():
            raise ValueError("Name must be a non-empty string containing only letters.")
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("PIN must be exactly 4 digits.")
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        account_number = self.next_account_number
        self.accounts[account_number] = Account(name, pin, initial_balance)
        self.next_account_number += 1
        return account_number


    def login(self, account_number: int, pin: str) -> Account:
        ''' if account was created then you will login with your valid credentials'''

        account = self.accounts.get(account_number)
        if not account or not account.check_pin(pin):
            raise ValueError("Invalid account number or PIN.")
        return account

    def balance_inquiry(self, account: Account) -> float:
        ''' you will get the balance of your account '''
        return account.balance

    def withdraw(self, account: Account, amount: float):
        ''' withdraw amount from balance make sure withdrawal amount must be positive else you will not withdraw amount
            if insufficient funds are available '''
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if account.balance - amount < 0:
            raise ValueError("Insufficient funds for withdrawal.")
        account.update_balance(-amount)
        account.add_transaction("Withdrawal", amount)

    def deposit(self, account: Account, amount: float):
        ''' entered amount to deposit, make sure that you entered positive amount'''
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        account.update_balance(amount)
        account.add_transaction("Deposit", amount)


    def update_account_info(self, account: Account, new_name: str = None, new_pin: str = None):
        ''' update information of user'''
        if new_name:
            account.update_name(new_name)
        if new_pin:
            account.update_pin(new_pin)

    def get_transaction_history(self, account: Account):
        return account.transaction_history


class Operation:
    atm=ATM()
    def choice_create_account(self):
        name = input("Enter your name: ")
        pin = input("Enter a 4-digit PIN: ")
        initial_balance = float(input("Enter initial balance: "))
        account_number = self.atm.create_account(name, pin, initial_balance)
        print(f"Account created successfully. Your account number is {account_number}.")
    
    def choice_login(self):
        account_number = int(input("Enter your account number: "))
        pin = input("Enter your PIN: ")
        account = self.atm.login(account_number, pin)
        print(f"Welcome, {account.name}!")

        while True:
            print("\nChoose an option: \n1. Balance Inquiry \n2. Withdraw \n3. Deposit \n 4. Update Account Information \n5. Transaction History \n6. Logout")
            user_choice = int(input("Enter choice: "))

            if user_choice == 1:
                print(f"Your account balance is: ${self.atm.balance_inquiry(account):.2f}")

            elif user_choice == 2:
                amount = float(input("Enter amount to withdraw: "))
                self.atm.withdraw(account, amount)
                print(f"${amount:.2f} withdrawn successfully. New balance: ${account.balance:.2f}")

            elif user_choice == 3:
                amount = float(input("Enter amount to deposit: "))
                self.atm.deposit(account, amount)
                print(f"${amount:.2f} deposited successfully. New balance: ${account.balance:.2f}")

            elif user_choice == 4:
                new_name = input("Enter new name (or press enter to skip): ")
                new_pin = input("Enter new PIN (or press enter to skip): ")
                self.atm.update_account_info(account, new_name if new_name else None, new_pin if new_pin else None)
                print("Account information updated successfully.")

            elif user_choice == 5:
                history = self.atm.get_transaction_history(account)
                if history:
                    print("\nTransaction History:")
                    for transaction in history:
                        print(f"{transaction['date']} - {transaction['type']}: ${transaction['amount']:.2f}")
                else:
                    print("No transactions found.")

            elif user_choice == 6:
                print("Logged out successfully.")
                break

            else:
                print("Invalid option. Please try again.")


def main():
    operations=Operation()
    while True:
        try:
            print("\nWelcome to the ATM. Choose an option:")
            print("1. Create Account")
            print("2. Login")
            print("3. Exit")
            choice = int(input("Enter choice: "))

            if choice == 1:
                operations.choice_create_account()

            elif choice == 2:
                operations.choice_login()

            elif choice == 3:
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
