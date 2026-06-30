""" 
modules - pull in python stnadard libraries
"""

import math
from random import randint,choice,seed
from  datetime as dt
print(math.pi)
print(math.sqrt(144))
print(math.ceil(4.1))

print(randint(1,6))
print(choice(["Rock", "pepar","scissors"]))

# new_year = dt.date(today.yera,12,31)
my_bday = dt.date(2000,12,12)
print(my_bday)



user = {"name":"arjit","skills":["py","ai"]}
text = json.dumps(user)
print("user",user(user))
print("user JSON", text)
back = json.loads(text)










