"""
###### Threading ######

    - Data sharing
"""

"""
Since processes dont share the same memory space, they dont have access to the same public data. Bcuz of that, they need a special shared memory objects.

Data can be stored in a shared memory variable using Value or Array.
    - Value(type, value): Create a ctypes object of type type.                  -> object.value
    - Array(type, value): Create a ctypes array with elements of type type.     -> array[n]
"""

from multiprocessing import Process, Value, Array
import time

def add_100(number):
    for _ in range(100):
        time.sleep(0.01)
        #Access the value of the given shared object by .value
        number.value += 1

def add_100_array(numbers):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            #Access the value of array item using the index
            numbers[i] += 1


if __name__ == "__main__":

    #Creates a shared Value of type integer and value 0
    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    #Creates a shared array of type decimal and the listed values
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    #Nothing new under the sun
    process1 = Process(target=add_100, args=(shared_number,))
    process2 = Process(target=add_100, args=(shared_number,))

    process3 = Process(target=add_100_array, args=(shared_array,))
    process4 = Process(target=add_100_array, args=(shared_array,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    print('Value at end:', shared_number.value)
    print('Array at end:', shared_array[:])

    print('end main')