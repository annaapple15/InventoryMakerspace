#account class

class Account():
    def __init__(self, name, balance, password):
        self.name = name
        self.balance = int(balance)
        self.password = password

    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        
        self.balance = self.balance + amountToDeposit
        return self.balance
    
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None
        
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        
        self.balance = self.balance - amountToWithdraw
        return self.balance
    
    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance
    #added for debugging
    def show(self):
        print('\tName:', self.name)
        print('\tBalance:', self.balance)
        print('\tPassword:', self.password)
        print()


oAccount = Account('Joe Schmoe', 1000, 'magic')

newBalance = oAccount.deposit(500, 'magic')