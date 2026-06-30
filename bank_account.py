class BankAccount:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("insufficient Fund")
        else:
            self.balance -= amount

class SavingAccount:
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance
        self.interest_rate = 0.06
        
    def withdraw(self, amount):
        if amount > self.balance * 0.3:
            print("Cannot withdraw more than 30% of the balance")
        else:
            self.balance -= amount
            
    class CurrentAccount(BankAccount):
        def __init__(self,account,balance):
            self.account = account
            self.balance = balance
            self.interest_rate = 0.02
            
        def deposit(self, amount):
            if amount > 300000:
                print("Cannot deposit more than 300k")
            else:
                self.balance -= amount
            
class LoanAccount(BankAccount):
    def __init__(self,account,balance):
        self.account = account
        self.balance = balance
        
        