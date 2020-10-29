"""
##### Basic Collection Data Types in Python #####
    
    *Lists  -> collection which is ordered and mutable. Allows duplicate members.
    *Tuple  -> collection which is ordered and immutable. Allows duplicate members.
    *Set    -> collection which is unordered and unindexed. No duplicate members.
    *Dict   -> collection which is unordered, mutable and indexed. No duplicate members.
    *String -> immutable sequences of Unicode code points.

"""

### LIST
###
# Creating a list
my_list = ['Item1', 'Item2', 'Item3']

# Creating an empty list
my_list = list()

# Lists allows different data types
my_list = ['Item1', True, 5]

# Lists allows duplicates
my_list = ['Item1', 'Item2', 'Item2']

# Items in lists
item = my_list[0]

# Item from reverse list
item = my_list[-1]

# Change item value
my_list[2] = "lemon"

# Useful methods
len(my_list)                #Returns the length of the list
my_list.append("Item5")     #Adds a new item at the end of the list
my_list.insert(1, "Item6")  #Adds a new item at specified index
my_list.pop()               #Removes the last item
my_list.remove("Item1")     #Remove speficied item
my_list.clear()             #Clear the list
my_list.reverse()           #Reverse the list
my_list.sort()              #Sort the list
my_list = [0] * 5           #Adds "0" 5 times

# Copying a list
my_list2 = my_list          #Points to the same memory location
my_list2 = my_list.copy()   #Copy the list as a new list

# Nested lists
my_list = [
    [1,2,3,4],
    [5,6,7,8]
]

### TUPLE
###
# Creating a tuple
my_tuple = (2, 1, "yeah", True)

# Creating a empty tuple
my_tuple = tuple()

# Items in tuples
item = my_tuple[1]

# Tuple with only one element needs a , at the end
my_tuple = (5,)

# Tuple items cant be modified
my_tuple[5] = "aaaa"        #It will raise an Error -> 'tuple' object does not support item assignment

# Deleting a tuple
del my_tuple

# Useful methods
len(my_tuple)               #Return the of length of the tuple
my_tuple.count()            #Return the number of items
my_tuple.index("Item")      #Return "Item" index
my_tuple = tuple(my_list)   #Convert a list to a tuple
my_list = list(my_tuple)    #Convert a tuple to a list
string = tuple('hello')     #Convert a String to tuple

# Unpacking
my_tuple = "Item1", "Item2", "Item3"
a, b, c = my_tuple          #Unpack the tuple content to variables, it will obey the sequence of both
my_tuple = "Item1", "Item2", "Item3", "Item4", "Item5"
a, *b, c = my_tuple         #The * operator will get multiple elements

## TUPLE VS LIST
# Size
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")      # -> 104 bytes
print(sys.getsizeof(my_tuple), "bytes")     # -> 88 bytes

# Processing time
import timeit
print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))     # -> 0.12474981700000853
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))     # -> 0.014836141000017733

### DICT
###

# Creating a dict
my_dict = {
    'Key1': 'Value1',
    'Key2': 'Value2',
    'Key3': 5
}

# Creating a dict with class constructor
my_dict = dict(key1='Value1', key2='Value2', key3=5)

# Creating a empty dict
my_dict = dict()

# Items in dict
item = my_dict['key']      #If key doesnt exist will raise an error -> KeyError: 'variablename'

# Add item
my_dict['key4'] = 'Content'

# Modify and item
my_dict['key1'] = 'Value2'

# Delete an item
del my_dict['key2']

# Useful methods
my_dict.pop("Key1")
my_dict.popitem()
my_dict.clear()

# Copying a dict
my_dict2 = my_dict              #Points to the same memory location
my_dict2 = my_dict.copy()       #Creates a new dict

# Merge two dicts
my_dict.update(my_dict2)

# Nested dicts
my_dict = {
    'dict1': {'key1': 1,
              'key2': 2},

    'dict2': {'key3': 3,
              'key4': 4}
}

### SET
###

# Creating a Set
my_set = {"Value1", "Value2", "Value3"}

# Creating an empty Set
my_set = set()

# Add items
my_set.add("Value4")

# Remove elements
my_set.remove("Value4")     #Raises an error if item doesnt exist -> KeyError 
my_set.discard("Value4")    #Wont do nothing if item doenst exist
my_set.clear()              #Clear all elements
my_set.pop()                #Return and remove a random element

# Operations
my_set = {"Value1", "Value2", "Value3"}
my_set2 = {"Value4", "Value5", "Value6"}

my_set.union(my_set2)                   #Combine elements of both sets without duplication !!Doesnt affect any of them!!
my_set.intersection(my_set2)            #Take elements that are in both sets !!Doesnt affect any of them!!
my_set.difference(my_set2)              #Returns a set with all elements of my_set that are not in my_set2 !!my_set2.difference(my_set) returns a different result!!
my_set.symmetric_difference(my_set2)    #Returns a set with all elements that are in my_set and my_set2 but are not in both

# Update
my_set.update(my_set2)                          #Updates the set with elements of another set
my_set.difference_update(my_set2)               #Updates the set removing elements found on another set
my_set.intersection_update(my_set2)             #Updates the set keeping only elements found in both
my_set.symmetric_difference_update(my_set2)     #Updates the set keeping onlye elements found in either set but not in both

# Copying sets
my_set2 = my_set              #Points to the same memory location
my_set2 = my_set.copy()       #Creates a new set

# Subset, Superset and Disjoint
my_set.issubset(my_set2)        #Return True if my_set contains my_set2
my_set.issuperset(my_set2)      #Return True if my_set is inside my_set2
my_set.isdisjoint(my_set2)      #Return True if there are no same elements

# Frozen set
my_frozenset = frozenset(my_set)        #Creates an immutable set from an iterable

### STRINGS
###

# Creating a string
my_string = 'String'

# Get a single char
char = my_string[0]

# Concatenate
char = ' '
my_string = 'String' + char + 'String2'

# Useful methods
my_string.strip()               #Remove the whitespaces
len(my_string)                  #Return the length of string
my_string.upper()               #Makes the string all uppercase
my_string.lower()               #Makes the string all lowercase
my_string.endswith('g')         #Return True if the given string endswith 'g'
my_string.startswith('S')       #Return True if the given string startswith 'S'
my_string.find('r')             #Return the first index of 'r' or -1 if None
my_string.count('i')            #Return how many 'i' string have
my_string.replace('r', 'a')     #Replace all 'r' by 'a' of given string
my_string.split(' ')            #Create a list element separating the string by ' '
my_string.join(my_list)         #Join elements of a iterable to a string, my_string became the separator

## !! Concatenating a string makes python create a new one and clone both of them meaning that use the + costs more !!
## !!                         Join method is much more efficient and faster, rather use it instead                  !!

## Format
# Placeholders
my_string = "Hello {0} and {1}".format("Bob", "Tom")
print(my_string)    # -> Hello Bob and Tom

my_string = "Hello {} and {}".format("Bob", "Tom")
print(my_string)    # -> Hello Bob and Tom

my_string = "The integer value is {}".format(2)
print(my_string)    # -> The integer value is 2

my_string = "The float value is {0:.3f}".format(2.1234)
print(my_string)    # -> The float value is 2.123

my_string = "The float value is {0:e}".format(2.1234)
print(my_string)    # -> The float value is 2.123400e+00

my_string = "The binary value is {0:b}".format(2)
print(my_string)    # -> The binary value is 10

# f Strings
name = 'Vinicius'
age = 18
my_string = f"Hello {name}. You are {age} years old"
print(my_string)    # -> Hello Vinicius. You are 18 years old

pi = 3.14159
my_string = f"Pi is {pi:.3f}"
print(my_string)    # -> Pi is 3.142

