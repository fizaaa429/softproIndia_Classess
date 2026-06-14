for ch in "python":
    print("letter:",ch)
    
students = ["Asha","Rohan","Chetan","Diya"]

for student in students:
    print("Welcome", student)
        
# task total cart value calculatot 
cart_prices = [300,499,55,2000]
total = 0
for price in cart_prices:
    total += price
print(f"toatl cart amount : {total}")            

leaderboard  = ["fiza","sneha","preeti"]
for rank,name in enumerate(leaderboard, start=1):
    print(f"# {rank} : {name}")
    
# task : for a given list of price new prices
# with 10% discount
cart_price = [300,499,88,2000]
discount = [price*0.9 for price in cart_price]
print(discount)    