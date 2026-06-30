main class - bankaccount
sub class - saving acount, current account, loan account
saving account - cannot withdrwan more then 30% interest 
rate 6%
current account - can withdrawn any amount
ca - interest rate 2% and , cannot deposit more theen 300k
loan account - cannot withdrawn

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
    
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.06

    def withdraw(self, amount):
        if amount > self.balance * 0.3:
            print("Cannot withdraw more than 30% of the balance")
        else:
            super().withdraw(amount)
        
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)
        self.interest_rate = 0.02

    def deposit(self, amount):
        if amount > 300000:
            print("Cannot deposit more than 300k")
        else:
            super().deposit(amount)

class LoanAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        print("Cannot withdraw from a loan account")


saving_acc = SavingAccount("SA123", 10000)  
saving_acc.withdraw(4000)
current_acc = CurrentAccount("CA123", 5000)
current_acc.deposit(350000)
loan_acc = LoanAccount("LA123", 20000)
loan_acc.withdraw(5000)

    