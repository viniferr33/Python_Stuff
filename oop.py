"""
##### Oriented Object Programing #####

    *Classes/Objects    -> A user defined prototype/blueprint and its methods, behavior and attributes
    *Inheritance        -> Allows a class to inherit methods, behavior and attributes from another class
    *Encapsulation      -> Put restrictions on methods and variables to prevent accidents
    *Polymorphism       -> Using diferent class types in the same way to optimize code
    *Special Functions  -> Methods used when centain syntax is used
    *Classmethod        -> Classmethod decorator bounds a method to a class rather than its object, very often used when you have to call a method but you dont have the object yet
    *Staticmethod       -> Staticmethod decorator bounds a method to a class rather than object, but static doenst know about the other class attributes, often used to group a util function to a class
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

class Truck(Vehicle):   #That is the child class with inherited methods and attributes from Vehicle, it could receive more than 1 Parent and inherit its methods too
    
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

### Special Functions
###
class Point:
    """Creates a cartesian point"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"      #Everytime the object is called as a String this method will be called

    def __add__(self, other):               #Every time the object is sum to another this method will be called
        x = self.x + other.x                
        y = self.y + other.y
        return Point(x, y)                  #This method sums 2 points

"""
#### Special Functions list ####

    #Operator                       #Expression            #Internally
    - Addition                  ->   p1 + p2        =       p1.__add__(p2)
    - Subtraction               ->   p1 - p2        =       p1.__sub__(p2)
    - Multiplication            ->   p1 * p2        =       p1.__mul__(p2)
    - Power                     ->   p1 ** p2       =       p1.__pow__(p2)
    - Division                  ->   p1 / p2        =       p1.__truediv__(p2)
    - Floor Division            ->   p1 // p2       =       p1.__floordiv__(p2)
    - Modulo                    ->   p1 % p2        =       p1.__mod__(p2)
    - Bitwise Left Shift        ->   p1 << p2       =       p1.__lshift__(p2)
    - Bitwise Right Shift       ->   p1 >> p2       =       p1.__rshift__(p2)
    - Bitwise AND               ->   p1 & p2        =       p1.__and__(p2)
    - Bitwise OR                ->   p1 | p2        =       p1.__or__(p2)
    - Bitwise XOR               ->   p1 ^ p2        =       p1.__xor__(p2)
    - Bitwise NOT               ->   ~p1            =       p1.__invert__()
    - Less Than                 ->   p1 < p2        =       p1.__lt__(p2)
    - Less Than or Equal To     ->   p1 <= p2       =       p1.__le__(p2)
    - Equal To                  ->   p1 == p2       =       p1.__eq__(p2)
    - Not Equal To              ->   p1 != p2       =       p1.__ne__(p2)
    - Greater Than              ->   p1 > p2        =       p1.__gt__(p2)
    - Grater Than or Equal To   ->   p1 >= p2       =       p1.__ge__(p2)
"""

pt = Point(4, 8)
print(pt)           # -> (4, 8)
pt2 = Point(9, -2)
print(pt+pt2)       # -> (13, 6)

### Classmethod
###
from datetime import date

class Person:
    def __init__(self, name, age):                          #To create a person you need to know the name and the age
        self.name = name
        self.age = age
                                                            #Class methods are often used as factory methods
    @classmethod                                            #This decorator makes the fromBirthYear a class method
    def fromBirthYear(cls, name, birthYear):                #This method can be called using the class rather than an Object
        return cls(name, date.today().year - birthYear)     #This method will return a Person object calculating its age

    def display(self):
        print(self.name + "'s age is: " + str(self.age))

Person.fromBirthYear('John', 2002).display()                # -> John's age is 18

### Staticmethod
###
class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod                           #This decorator makes the toDashDate a static method
    def toDashDate(date):                   #This method doesnt interact with the class attributes, it behaves like a commom function, but its grouped in "Dates"
        return date.replace("/", "-")

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)     # Replace every '/' by a '-'

date.getDate() == dateWithDash      # -> True

"""
### Diference between Static and Class methods ###
    - Static method knows nothing about the class and just deals with the parameters
    - Class method works with the class since its parameter is always the class itself.
    - Class method works well with inheritance, Static doesnt
"""
