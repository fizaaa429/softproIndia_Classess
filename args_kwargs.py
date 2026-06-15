""" 
*args (extra positionals -> tuple)
**kwargs (extra keywords)
"""

def total(*args):
    print(" args is a tuple", args)
    return sum(args)

print("total (10,20,30) =", total(10,20,30))
print("total (10,250) =", total(10,250))
print("total () =", total())



def make_user(**kwargs):
    print(" kwargs is a dict", kwargs)
    return kwargs

make_user(name="fiza", age=22,city="bareilly")
make_user(name="ben")