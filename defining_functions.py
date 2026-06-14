""" 
Defining function - block of code that can be reused
"""
def great():
    """print a friendly greeting""" #docstring - one line
    print("hello , welcome to your course!!!")

great()
great()    


#print(great())
print(great.__doc__)


def say_bye():
    """sign off"""
    print("see you tomorrow")
    
say_bye()    