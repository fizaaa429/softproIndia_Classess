""" parameters(names in def) - arguments (value you pass)
"""
def great(name):
    """great one person by name"""
    print(f"hello {name}")
    
great("ben")
# arguments can be expressions
raw = "  chetan  "
great(raw.strip().title())    


#multipe parameters -> matched by postions
def book_ticket(name,seat,price):
    """print a book line"""
    print(f"{name} -> seat : {seat} (Rs {price}")
    
book_ticket("arjit","38",900)    

orders = [101,102,103]

def confirm_order(order_id):
    print(f"order #{order_id} confirment.out for delivery")
    
for old in orders:
    confirm_order(old)    
    
    