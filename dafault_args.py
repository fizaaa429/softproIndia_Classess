
def add_cart_item(item,cart=[]):
    cart.append(item)
    return cart

print(" ", add_cart_item("Apple"))
print(" ", add_cart_item("banana"))
print(" ", add_cart_item("bread"))

def add_cart(item_cart=None):
    if cart is None:
        cart = []
    cart.append(item)
    return add_cart
print(" ", add_cart("apple"))
print(" ", add_cart("banana"))
print(" ", add_cart("bread"))    
    


   