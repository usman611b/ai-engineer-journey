from abc import ABC, abstractmethod
class  Account(ABC):
    def __init__(self, account_number,owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount.")
    def get_balance(self):
        return self.__balance
    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def __init__(self, account_number, owner_name, balance, interest_rate):
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.get_balance() * self.interest_rate / 100
        print(f"Interest for Savings Account: {interest}")
        return interest
class CurrentAccount(Account):
    def __init__(self, account_number, owner_name, balance, overdraft_limit):
        super().__init__(account_number, owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def calculate_interest(self):
        print("Current accounts do not earn interest.")
        return 0
class Bank:
    def __init__(self , bank_name ):
        self.bank_name = bank_name
        self.customers = []
        self.accounts = []
    def add_account(self, account):
        self.accounts.append(account)
    def add_customer(self, customer):
        self.customers.append(customer)
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                print(f"Account found: {account.account_number}, Owner: {account.owner_name}, Balance: {account.get_balance()}")
                return account
        print("Account not found.")
        return None
    def find_customer(self, customer_name):
        for customer in self.customers:
            if customer.name == customer_name:
                print(f"Customer found: {customer.name}, ID: {customer.customer_id}")
                return customer
        print("Customer not found.")
        return None
    def  close_account(self, account_number):
        account = self.find_account(account_number)
        if account:
            self.accounts.remove(account)
            return
        else:
            return "Account not found."
    def display_all_accounts(self):
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Owner: {account.owner_name}, Balance: {account.get_balance()}")
    def display_all_customers(self):
        if not self.customers:
            print("No customers found.")
        for customer in self.customers:
            print(f"Customer Name: {customer.name}, Customer ID: {customer.customer_id}")
            
class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.accounts = []
        self.customer_id = customer_id
    def display_info(self):
        print(f"Customer Name: {self.name}, Customer ID: {self.customer_id}")

    def customer_account_info(self):
        print(f"Customer Name: {self.name}, Customer ID: {self.customer_id}")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.get_balance()}")

    #Association between Customer and Account
    def add_account(self, account):
        if isinstance(account, Account):
            self.accounts.append(account)
        else:   
            print("Invalid account. Must be an instance of Account class.") 
    
#Now we can create instances of the Bank, Customer, and Account classes and demonstrate their functionality.
account1 = SavingsAccount("SA123", "Alice", 1000, 5)
account2 = CurrentAccount("CA456", "Bob", 2000, 500)
bank = Bank("HBL_Bank")
customer1 = Customer("Alice", "C001")
customer2 = Customer("Bob", "C002") 

bank.add_account(account1)
bank.add_account(account2)

bank.add_customer(customer1)
bank.add_customer(customer2)    

bank.display_all_accounts()


bank.find_account("SA123")

account1.deposit(500)
account1.withdraw(200)

bank.display_all_accounts()
customer1.add_account(account1)
customer1.display_info() #
account1.calculate_interest()

account3 = SavingsAccount("SA789", "Charlie", 1500, 4)
bank.add_account(account3)
customer1.add_account(account3) # c
bank.display_all_accounts()
account3.owner_name
customer1.customer_account_info()
 #Invalid case for customer trying to add an account that is not an instance of Account class
customer1.add_account("NotAnAccount")  # Invalid case for customer trying to add an account that is not an instance of Account class

for account in bank.accounts:
    account.calculate_interest()