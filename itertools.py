"""
##### Iterator handling tools #####

    *Infinite iterators       -> Runs infinitely or until reach an endcondition
        - count()
        - cycle()
        - repeat()
    
    *Short iterators          -> Runs until reach the end of iterable items in it    
        - accumulate()
        - chain()
        - chain.from_iterable()
        - compress()
        - dropwhile()
        - filterfalse()
        - groupby()
        - islice()
        - starmap()
        - takewhile()
        - tee()
        - ziplongest()

    *Combinatoric iterators   -> Perform combinatoric operations
        - product()
        - permutations()
        - combinations()
        - combinations_with_replacement()
"""

### Count
###
from itertools import count
count(0, 1)             #Returns an infinite iterator which starts at '0' and is spaced by '1'

### Cycle
###
from itertools import cycle
cycle([2,5,4,3,6])      #Return an infinite iterator which iterates through each element and produces the sequence -> 2 5 4 3 6

### Repeat
###
from itertools import repeat
repeat("Object", 2)     #Return an iterator with the same object infinite or specified times

### Accumulate
###
import operator
from itertools import accumulate
accumulate([5,4,8,6,7], operator.add)     #Return an iterator with the sum of all operations specified by operator -> [5, 9, 17, 23, 30]

### Chain
###
from itertools import chain
chain('ABC', 'DEF')         #Return a iterator which contains the elements of N iterators passed as arguments -> 'ABCDEF'

### Chain from iterable
###
chain.from_iterable(['ABC', 'DEF'])     #Do the same of chain but with a iterable of iterables

### Compress
###
from itertools import compress
compress('ABCDE', [1,0,1])              #Return an iterator with corresponding data from both iterators which evaluates to True -> A C 

### Dropwhile
###
from itertools import dropwhile
def menorq3(x):
    return x < 3

dropwhile(menorq3, [5, 2, 0, 8])        #Return the elements which statement tests True, afterwards return every element -> [5, 8, 2, 0]

### Filterfalse
###
from itertools import filterfalse
filterfalse(lambda x: x<5, range(10))   #Return an iterable which statement tests False -> [5, 6, 7, 8, 9]

### Groupby
###
from itertools import groupby
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, 
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
groupby(persons, key=lambda x: x['age'])    #Return an iterable with groups of items in lambda func
                                            # -> 25 [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}]
                                            # -> 27 [{'name': 'Lisa', 'age': 27}]
                                            # -> 28 [{'name': 'Claire', 'age': 28}]

groupby(["hi", "nice", "hello", "cool"], key=lambda x: "i" in x)    # e.g -> will return every word which have "i" in group True
                                                                    # True ['hi', 'nice']
                                                                    # False ['hello', 'cool']

### Islice
###
from itertools import islice
islice(range(10), 2, 2, 5)      #Return an iterable with all items from a given iterable between '2' with step '2' and ending in '5' -> [2, 4]

### Starmap
###
from itertools import starmap
starmap(pow, [(2,5), (3,2), (10,3)])    #Return an iterable that computes results of a given function with organized parameters in tuples with the same number of argumens
                                        # -> 32, 9, 1000

### Takewhile
###
from itertools import takewhile
takewhile(lambda x: x<5, [1,4,6,4,1])   #Return items from iterator while statement is True -> [1,4]

### Tee
###
from itertools import tee
tee('abcdef', 4)                        #Return '4' iterators with same items of given iterable

### Ziplongest
###
from itertools import zip_longest
zip_longest([5,2,4], [8,5,8,6], fillvalue='')     #Return a zip of two given iterables but will continue until the longest iterable ends -> (5,8) (2,5) (4,8) (6,'')

### Product
###
from itertools import product
product('ABCD', 'xy')       #Return the cartesian product of given -> Ax Ay Bx By Cx Cy Dx Dy
product(range(2), repeat=3) # -> 000 001 010 011 100 101 110 111

### Permutations
###
from itertools import permutations
permutations(range(3))  #Return all permutations between iterable items -> 012 021 102 120 201 210

### Combinations and Combinations w replacement
###
from itertools import combinations, combinations_with_replacement
combinations([1, 2, 3, 4], 2)                   #Return all combinations without replacement -> [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
combinations_with_replacement([1, 2, 3, 4], 2)  #Return all combinations with replacement -> [(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]

