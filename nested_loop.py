""" 
Nested loop - a loop inside a loop
"""
# Mental model Rows X cols
for row in range(3):
    for col in range(4):
        print()
        

colors = ["Red","Blue"]
sizes = ["s","m","l"]
print("Generate Variants")
for color in colors:
    for size in sizes:
        print(f" {color} / {size}")
                       