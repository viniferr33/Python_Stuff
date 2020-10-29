"""
##### Advanced Collection Data Types in Python #####

    *Counter     -> Dict subclass for counting hashable objects
    *namedTuple  -> Factory function for creating tuple subclasses with named fields
    *OrderedDict -> Dict subclass that remembers the order entries were added
    *defaultdict -> Dict subclass that calls a factory function to supply missing values
    *deque       -> Double-Queued list
    *ChainMap    -> Wraps N Dicts to a updatable dict which allows to treat multiple dicts as one
    *heapq       -> Creates a data structure with a self-updated priority queue
    
    *UserDict    -> Useful to create a dict-inherit class with modified behavior
    *UserList    -> Useful to create a list-inherit class with modified behavior
    *UserString  -> Useful to create a string-inherit class with modified behavior

"""

### Counter
###
# Creating a counter
from collections import Counter
x = "An Iterable"
my_counter = Counter(x)     #Creates dict which stores the element as a key and how many times it appear as value
print(my_counter)           # -> Counter({'e': 2, 'A': 1, 'n': 1, ' ': 1, 'I': 1, 't': 1, 'r': 1, 'a': 1, 'b': 1, 'l': 1})

# Useful methods
my_counter.items()          #Return the dict items as tuples
my_counter.keys()           #Return the dict keys as a list
my_counter.values()         #Return the dict values as a list 
my_counter.most_common(2)   #Return the '2' most commom elements of my_counter

### namedTuple
###
# Creating a namedTuple
from collections import namedtuple
Name = namedtuple("Name", 'x', 'y', 'z')    #Creates lightweight object type. Takes the first argument as the typename and the following N arguments as fields of it
nm = Name(1, 2, 3)
print(nm.x)         # -> 1
print(nm.y)         # -> 2
print(nm.z)         # -> 3

### OrderedDict
###
# Creating a OrderedDict
from collections import OrderedDict
ordered_dict = OrderedDict()    #Creates a commom dict but it will remember the order of entrys

### defaultdict
###
# Creating a defaultdict
from collections import defaultdict
default_dict = defaultdict(int)     #Creates a commom dict but it will only accept specified type values

### deque
###
# Creating a deque
from collections import deque
deq = deque()           #Creates a double-queued list which means that methods could be applied from both sides

# Useful methods
deq.append("A")         #Adds 'A' to the right side
deq.appendleft("B")     #Adds 'B' to the left side

deq.pop()               #Removes the last item from the right side
deq.popleft()           #Removes the last item from the left side

deq.extend(['C', 'D', 'E'])         #Add the list elements at the right side
deq.extendleft(['F', 'G', 'J'])     #Add the list elements at the left side

deq.rotate(-2)          #Moves all items '-2' steps
deq.count('A')          #Counts how many 'A'
deq.clear()             #Remove all items

### ChainMap
###
# Creating a ChainMap
from collections import ChainMap
dict1 = {
    'Key1': 'Value1',
    'Key2': 'Value2',
    'Key3': 5
}

dict2 = {
    'Key4': 'Value3',
    'Key5': 'Value4',
    'Key6': 10
}

dictall = ChainMap(dict1, dict2)        #Created a new dict with Keys and values from both dicts
print(dictall['Key1'])                  # -> Value1
print(dictall['Key6'])                  # -> 10

dict1['Key10'] = "Value10"              #Updating any of those chained dicts
print(dictall['Key10'])                 # -> Value10    //     The ChainMap will point to updated dict

### HeapQueue
###
# Creating a HeapQueue
import heapq
list1 = [5, 7, 9, 1, 3]
heapq.heapify(list1)            #Convert list1 into a Heap
heapq.heappush(list1, 4)        #Push 4 elements into Heap
print(list(list1))              # -> [1, 3, 4, 7, 5, 9]             // Heap could be converted into list type to be workable
heapq.heappop(list1)            #Return and remove the smalest element
heapq.heappushpop(list1, 2)     #Push and Pop simultaneosly
heapq.heapreplace(list1, 2)     #Pop first and Push after
heapq.nlargest(3, list1)        #Return the first '3' largest elements
heapq.nsmallest(3, list1)       #Return the first '3' smallest elements

### UserDict
###
# Creating a UserDict
from collections import UserDict
dict1 = {
    'Key1': 'Value1',
    'Key2': 'Value2',
    'Key3': 5
}
user_dict = UserDict(dict1)
user_dict.data      #Access the dict1 content

## Creating a dict class with modified behavior -> Deletion not allowed
class MyDict(UserDict): 
      
    # Function to stop deletion 
    def __del__(self): 
        raise RuntimeError("Deletion not allowed") 
          
    # Function to stop pop
    def pop(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Function to stop popitem  
    def popitem(self, s = None): 
        raise RuntimeError("Deletion not allowed") 

### UserList
###
# Creating a UserList
from collections import UserList
list1 = [1,2,3,4,5]
user_list = UserList(list1)
user_list.data      #Access the list1 content

## Creating a list class with modified behavior -> Deletion not allowed
class MyList(UserList): 
      
    # Function to stop deleltion 
    def remove(self, s = None): 
        raise RuntimeError("Deletion not allowed") 
          
    # Function to stop pop
    def pop(self, s = None): 
        raise RuntimeError("Deletion not allowed") 

### UserString
###
# Creating a UserString
from collections import UserString
string1 = "asgjfgsafsaguifauifa"
user_string = UserString(string1)
user_string.data    #Access the string1 content

## Creating a string class with modified behavior -> Mutable String
class Mystring(UserString): 
      
    # Function to append
    def append(self, s): 
        self.data += s 
          
    # Function to remove  
    def remove(self, s): 
        self.data = self.data.replace(s, "") 