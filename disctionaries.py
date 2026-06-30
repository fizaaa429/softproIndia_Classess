""" 
dict - key:value pair , look 
not position
"""
student = {
    "name":"fiza",
    "age":21,
    "marks":[88,43,23]
}

print("name:    ",student["name"])
print("How many items in dict:", len(student))
print("'age' in student", "age" in student)
#print("missing values" , student["collage"])
print("missing values" , student.get("collage"))

student["email"] = "abc@gamil.com"
student["age"] = 21
print("student after update", student)

removed_item = student.pop("marks")
print(removed_item)

del student["email"]
#task - create the total bill 
prices = {
    "coffee":120,
    "juice":100,
    "sandwich":150
}
order = ["coffee,juice"] 

total_bill = 0
for item in order:
    total_bill +=prices.get(item)
    
    
    
                    




