""" 
classes and objects - blueprint(class)->instance
(object)
"""
class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
rex = Dog("Rex","Labrador")
kallu = Dog("kallu","desi")


kallu.name = "Dogesh"      
print(rex.name,rex.breed)

#creat a clear student - name , rollno,email

class student:
    def __init__(self,name,rollno,email):
        self.name = NameError
        self.rollno = rollno
        self.email = email
s1 = student("fiza","22","idrishifiza456@gamil.com")
print(s1.name.rollno.email) 

s1.display()  
      



class BankAccuont:
    bank_name = "SBI"
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance
        return self.balance
    
    
tom = BankAccuont("Tom",1000)
ketan = BankAccuont("ketan")

tom.deposit(5000)
print(tom.balance)    
print(vars(tom))

            