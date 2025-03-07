class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self._interest_rate = 0.05  # Protected attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):  # Public method to access private data
        return self.__balance

# Creating an object
account = BankAccount("123456", 1000)

# Accessing public attribute
print(account.account_number)  # Output: 123456

# Accessing protected attribute (not recommended but possible)
print(account._interest_rate)  # Output: 0.05

# Trying to access private attribute (will cause an error)
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing private attribute using a public method
print(account.get_balance())  # Output: 1000

# Performing operations
account.deposit(500)  # Deposited $500. New Balance: $1500
account.withdraw(200)  # Withdrew $200. Remaining Balance: $1300
#account.withdraw(2000)  # Insufficient funds!
#print(account.get_balance())  # Output: 1300