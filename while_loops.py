"""
While Loop
"""
     
# Anatomy => init -> test -> update
    
count = 1

while count <= 5:
    print(f"Rep {count} of 5")
    count += 1

print("Done Counting\n")

count = 10
while count >= 1:
    print(f"Rep {count} of 10")
    count -= 1

print("Done Counting\n")



print("Tiny menu - type 'quit' to leave")
while True:
    choice = input("pick (status/help/quit)".strip().lower())
    if choice == "quit":
        print("Bye")
        break
    elif choice == "status":
        print("all system up")
        break
    elif choice == "help":
        print("commands : status,help , quit")
    else:
        print(f"unknown command : {choice}")    
        
    