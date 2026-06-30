""" 
try/except/else/finally
"""

def to_int(text):
    try:
        return int(text)
    except ValueError:
        return None
    
print(to_int(42))
print(to_int("ABC"))

def safe_divide(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print(f" {a}/{b} : cannot divide by zero")
    else:
        print(f"{a} / {b} = {result}") #runs onlyif no excentation
    finally:
        print(" Its Done") #finally runs

safe_divide(1,2)
safe_divide(4,5)
safe_divide(9,10)                    
    