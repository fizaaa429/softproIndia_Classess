""" 
default value
"""

def great(name,greeting = "hi"):
    print(f"{greeting} , {name}")

great("fiza")
great("fiza","welcome")    

#keyword arguments
def book_tickets(name,seat,price):
    print(f"{name} --> seat {seat} (rs {price})")
    
book_tickets("arjit","3b",899)   
book_tickets(name="arjit",price=899,seat="3b")
book_tickets("arjit",price=899,seat="3b")
   