"""
###### Generators #####

"""

# Syntax
###

def my_generator():
    yield 1                 # The 'yield' statement works like a return but it will pause the function soon as called
    yield 2                 # Calling the next method a generator leads to next yield
    print('Hey')
    yield 3

g = my_generator()          # Generator functions returns a generator object to control the actions, Generators are iterables
next(g)                     # This will yield the first value   -> 1
next(g)                     # This will yield the second value  -> 2
next(g)                     # This will yield the third value   -> 'Hey' 3
next(g)                     # This will raise an error -> StopIteration

# Memory
###
"""
Generators save memory, The value are generated only when needed and dont need to wait all the dataset to be processed
"""
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)
import sys
print(sys.getsizeof(firstn(1000000)), "bytes")

# Expression
###
mygen = (i for i in range(1000) if i % 2 == 0)          # This will return a generator

mygen = [i for i in range(1000) if i % 2 == 0]          # This will return a list

