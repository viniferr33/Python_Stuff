"""
##### Multiprocessing #####

    - Queued Processing
"""

"""
## What is a queue ##

A queue is a linear data structure that follows the First In First Out (FIFO) principle. A good example is a queue of customers that
are waiting in line, where the customer that came first is served first.

## Example ##
from multiprocessing import Queue

#Create queue
q = Queue()

#Add elements
q.put(1) # -> 1
q.put(2) # -> 2 1
q.put(3) # -> 3 2 1 

# Back --> 3 2 1 --> Front

#Get and remove first element
first = q.get() # --> 1
print(first) 

# Back --> 3 2 --> Front

## Important methods to use with Multiprocessing ##

    q.get() : Remove and return the first item. By default, it blocks until the item is available.
    q.put(item) : Puts element at the end of the queue. By default, it blocks until a free slot is available.
    q.empty() : Return True if the queue is empty.
    q.close() : Indicate that no more data will be put on this queue by the current process. 
"""

from multiprocessing import Process, Queue

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(i*-1)

if __name__ == "__main__":
    
    numbers = range(1, 6)
    q = Queue()

    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers,q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not q.empty():
        print(q.get())
        
    print('end main')