"""
##### Generators #####

    *Generators are functions that can be paused and resumed return an object that can be iterated over. 
    *Unlike lists, they are lazy and produce itens one at time and only when asked

    + Memory Efficient
"""

# Creating a generator
def my_gen():
    yield 1
    yield 2
    yield 3     #yield statement works like a return, but when the next method is called the program runs the code between the last yield and the next

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

# Using a generator
generator_obj = countdown(3)

print(next(generator_obj))      # -> Starting // 3
print(next(generator_obj))      # -> 2
print(next(generator_obj))      # -> 1
print(next(generator_obj))      # -> Raise an exception "StopIteration"

# Iterating
generator_obj = countdown(3)
sum_gen = sum(generator_obj)

for i in generator_obj:
    print(i)

## Memory Efficient objects
import sys

# Using list
def firstn(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(firstn(1000000))
print(sum_of_first_n)                           # 499999500000
print(sys.getsizeof(firstn(1000000)), "bytes")  # 8697464 bytes

# Using generator
def genfirstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = sum(genfirstn(1000000))
print(sum_of_first_n)                               # 499999500000
print(sys.getsizeof(genfirstn(1000000)), "bytes")   # 120 bytes
