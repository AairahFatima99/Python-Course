# Parent class
class dad:

    def __init__(self, eyes, aggressive):
        self.eyes = eyes
        self.aggresive = aggressive

    def display(self):
        print("Your eye color is", self.eyes)
        print("You are aggresive", self.aggresive)

# Child class 
class son(dad):

    def __init__(self, name, age, eyes, aggresive):
        self.name = name
        self.age = age

        # invoking the __init__of parent class
        # to access its attributes
        dad.__init__(self, eyes, aggresive)

# Object Creation
obj = son("Penguin", 8, "blue", True)

#Calling method display
obj.display()
