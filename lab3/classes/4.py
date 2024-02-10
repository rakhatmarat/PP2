class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposit of {} accepted".format(amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal of {} accepted".format(amount))
        else:
            print("Funds unavailable!")

owner = input("Enter account owner's name: ")
initial_balance = float(input("Enter initial balance: "))

account = Account(owner, initial_balance)

while True:
    action = input("Enter 'deposit' or 'withdraw' to perform transaction (or 'quit' to exit): ")
    if action == 'quit':
        break
    elif action == 'deposit':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif action == 'withdraw':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    else:
        print("Invalid action!")
