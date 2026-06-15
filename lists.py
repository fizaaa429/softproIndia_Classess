""" 
lists - ordered , changables collections.
"""


cart = ["milk","break","banana"]
print("cart : ",cart)
print("first item of cart", cart[0])
print("last item of cart", cart[-1])
print("length", len(cart))
print("slice" , cart[0:2])
print("'milk in cart'","milk" in cart)  


#mutating a list
cart[0] = "coffee"
print(cart)
cart.append("rice")
cart.insert(0,"tea")
shopping_list = ["jam","oil"]
cart.extend(shopping_list)
print(cart)



demo = [1,2]
demo.append([3,4])
print("demo after append",demo)
demo = [1,2]
demo.extend([3,4])
print("demo after extend",demo)

#Removing items

removed_item = cart.pop()
print(cart)
print(removed_item)
cart.remove("tea")
print("cart after removing tea", cart)
print("")
del cart[0]
print_queue = []
print_queue.append("report.pdf")
print_queue.append("invoice.pdf")
print_queue.append("photo.png")
print(f"{len(print_queue)} jobs waiting")
for job in print_queue:
    print(f"now printed : ",job)
    

