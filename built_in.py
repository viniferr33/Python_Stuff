"""
##### Built-In Functions #####

"""

### Abs
###
abs(-2.75)      #Return the absolute value of a given number -> 2.75

### All
###
all([True, False, True])    #Return True or False based on how many the iterable have the same value -> True

### Any
###
any([True, False, False])   #Return True if any of the iterable values is True -> True

### Ascii
###
ascii('Çopa pà noís')       #Return the given string in ASCII -> '\xc7opa p\xe0 no\xeds'

### Bin
###
bin(16)     #Return the given value in binary with 0b Prefix -> 0b10000

### Bool
###
bool(1)     #Return True unless the value is None, empty, 0 or False -> True

### Breakpoint -> Only works after 3.7 before that use pdb.set_trace()
breakpoint()    #Creates a debbug env which pauses the program and allows to check the variables !!type 'n' to go to next line, a var name to see its value

### Bytearray
###
bytearray('Source String', 'utf-16')    #Return the given source encoded by the given encoded method as a array, a third argument could be passed as a function to handle errors
                                        # -> b'\xff\xfeG\x00e\x00e\x00k\x00s\x00f\x00o\x00r\x00g\x00e\x00e\x00k\x00s\x00'

### Bytes
###
bytes(4)    #Return the given value as a immutable bytes object, the encoding method and the error handler function could be passed as well -> b'\x00\x00\x00\x00'

### Callable
###
callable(function)  #Return True if the given function is callable -> False

### Chr
###
chr(97)     #Return the string representing a character whose Unicode points to -> 'a'

### Compile
###
compile('print(55)', 'test', 'eval')    #Return the specified source code as object ready to be executed -> '55'
                                        #print(55) -> The source, could be a String, a Bytes object, or an AST object
                                        #test -> The name of the file that the source comes from. If the source does not come from a file, you can write whatever you like
                                        #eval -> The compile mode, it could be:
                                        #eval - if the source is a single expression; 
                                        #exec - if the source is a block of statements;
                                        #single - if the source is a single interactive statement;

### Complex
###
complex('3+5j')     #Return a complex number based on its expression -> (3+5j)
complex(3, 5)       # -> (3+5j)

### Delattr
###
delattr(object, 'attribute')    #Delete the given attribute from the object, equivalent to del object.attribute

### Dir
###
dir()           #Return all the methods and properties of the specified object, if is empty will refers to module namespace -> ['__builtins__', '__name__']

### Divmod
###
divmod(5, 2)    #Return a tuple with the quocient and the remainder -> (2, 1)

### Enumerate
###
enumerate(['Spring', 'Summer', 'Fall', 'Winter'], start=1)   #Return a list with tuples containing enumerated itens -> [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

### Eval
###
eval('print(55)')   #Evaluates the specified expression, if is a legal expression it will be executed

### Exec
###
exec('name = "John"\nprint(name)')  #Execute a specified python code, it accepts files, bytes and huge blocks of code.

### Filter
###
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

filter(myFunc, ages)       #Return the values which myFunc tests True -> 18, 24, 32

### Getattr
###
getattr(object, 'attribute')    #Return the value of the named attribute of object

### Globals
###
globals()       #Return a dictionary containing the current global symbols table

### Hasattr
###
hasattr(object, 'attribute')    #Return True if the given object has the attribute

### Hash
###
hash((1, 2, 3, 4, 5))      #return the hash value of the object -> 8315274433719620810

### Hex
###
hex(255)        #Return the given number in hexadecimal string with prefix 0x -> 0xff

### Id
###
id(object)      #Return the unique id of a given object

### isInstance
###
isinstance(object, 'class')     #Return True if the object is an instance of a given class

### isSubclass
###
issubclass('class', 'classinfo')    #Return True if the class is a subclass of a given class

### Iter
###
iter(["apple", "banana", "cherry"]) #Return a generic iterator which could be used in many ways
iter(function, 50)                  #Call the function until its value is equals to 50

### Locals
###
locals()    #Update and return a dictionary representing the current local symbol table

### Map
###
map(lambda x,y: x/y, [(5,3), (8,7), (6,8)])     #Return an itertator with the results of the given function and the given iterable

### Max
###
max([2,4,5,7,8,9,4,6,10,55])  #Return the largest item in an iterable

### Min
###
min([2,4,5,7,8,9,4,6,10,55])  #Return the smallest item in an iterable

### Oct
###
oct(8)    #Return the octal value of a given number -> 0o10

### Ord
###
ord('a')  #Return the Unicode intereger of a given Char -> 97

### Round
###
round(0.5, 1)   #Return the rounded number with the given amount of digits -> 0

### Setattr
###
setattr(object, 'attribute', 55)  #Set the attribute of a given object with the given value == object.attribute = 55

### Zip
###
zip([5,4,8,6,0,8], [8,5,7,6,4,8,1,7])     #Return a list of tuples containing the I element of N given iterables -> (5, 8) (4, 5) (8, 7) ...