"""
##### Oriented Object Programing #####

    *Classes/Objects    -> A user defined prototype/blueprint and its methods, behavior and attributes
    *Inheritance        -> Allows a class to inherit methods, behavior and attributes from another class
    *Encapsulation      -> Put restrictions on methods and variables to prevent accidents
    *Polymorphism       -> Using diferent class types in the same way to optimize code
    *Classmethod        -> Classmethod decorator 
    *Staticmethod       -> Staticmethod decorator
    *Meta Programming   -> 
"""

### Classes and Objects
###
class Parrot:       #A class is a blueprint for the object, containing all the details about the attributes and its behavior
    """Yo hoho iam a Pirate Parrot, and also a docstring, I will appear as description fo every parrot created"""
    #Class attributes
    species = "bird"        #Class attributes can be assigned by default on class which means that every "Parrot" will belong to "bird" species

    #Constructor
    def __init__(self, name, age):      #The Constructor will be called every time you create a new object of its class, self means that is a class method
        self.name = name                #Instance attributes
        self.age = age
    
    #Class method
    def sing(self, song):
        return f"{self.name} is singing {song}!"

    #Class method
    def dance(self):
        return f"{self.name} is dancing!"

    #Destructor
    def __del__(self):                  #The destructor is called to delete the object
        print(f"{self.name} died :(")

Blue = Parrot('John', 10)   #This is an object of Parrot type, which means Blue will have the species value = 'bird', name = 'John' and Age = 10
Red = Parrot('Mike', 22)    #This is an object of Parrot type, which means Red will have the species value = 'bird', name = 'Mike' and Age = 22

print(Blue.__class__.species)   # -> 'bird'
print(Red.name)                 # -> 'Mike'
print(Parrot.__doc__)           # -> 'Yo hoho iam a Pirate Parrot, and also a docstring, I will appear as description fo every parrot created'

Blue.sing('What is the brother?')   # -> John is singing What is the brother?!
Red.dance()                         # -> Mike is dancing!

del Blue        # -> John died :(

### Inheritance
###
class Vehicle:      #That will be the parent class

    def __init__(self, model, kilometers, fuel):
        self.model = model
        self.kilometers = kilometers
        self.fuel = fuel

    def travel(self, amount):
        self.kilometers += amount
        self.fuel -= amount
    
    def status(self):
        return f"The {self.model} has traveled {self.kilometers} and still have {self.fuel} of fuel"

class Truck(Vehicle):   #That is the child class with inherited methods and attributes from Vehicle
    
    def __init__(self, model, kilometers, fuel):
        #Super function allows to run the parent __init__ function inside Truck __init__ class
        super().__init__()

    def load(self, product, amount):    
        self.product = product
        self.amount = amount

Civic = Vehicle('Honda Civic', 0, 25)
Volvo = Truck('Volvo', 500500, 500)

Volvo.travel(300)
Volvo.status()      # -> The Volvo has traveled 501000 and still have 200 of fuel
Volvo.load('Rice', 2000)

### Encapsulation
###

class Computer:
    
    def __init__(self, user, password):
        self.user = user
        self.__password = password
    
    def changePass(self, newpass):
        self.__password = newpass

    def show(self):
        return f"The password of {self.user} is {self.__password}"

pc = Computer('Jerry', '87afa854')
pc.__password = '48445'     #Wont change nothing
pc.user = 'J3rR7 HckD!'     #Will change the value of user
pc.changePass('Ar84a7r')    #Will change the value of password

pc.show()                   # -> The password of J3rR7 HckD! is Ar84a7r

### Polymorphism
###

class Monkey:

    def climb(self):
        return "Monkey can climb the tree!!"

class Fish:

    def climb(self):
        return "Fish cant climb the tree!!"

#Commom interface between two classes
def can_climb(animal):
    animal.climb()

#Creating the objects
monke = Monkey()
fesh = Fish()

can_climb(monke)    # -> Monkey can climb the tree!!
can_climb(fesh)     # -> Fish cant climb the tree!!

### Classmethod
###
