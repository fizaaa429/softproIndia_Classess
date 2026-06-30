""" inheritance neuse a base class
"""

class animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        return",,,"
    
class dog(animal):
    def speak(self):
        return "woof"
    
class cat(animal):
    def speak(self):
        return "meow"

rex = dog("rex")
print(rex.speak())
luna = cat("luna")
print(rex.)    
                