"""
###### Threading ######

    - Data Locks
"""

"""

## Avoid race contitions ##

Because the thread scheduling, algorithm can swap between threads at any time, you don't know the order in which the threads will attempt
to access the shared data. In our case, the first thread accesses the database_value (0) and stores it in a local copy. It then increments
it (local_copy is now 1). With our time.sleep() function that just simulates some time consuming operations, the programm will swap to the
second thread in the meantime. This will also retrieve the current database_value (still 0) and increment the local_copy to 1. Now both 
threads have a local copy with value 1, so both will write the 1 into the global database_value. This is why the end value is 1 and not 2.

## Locks ##

A lock (also known as mutex) is a synchronization mechanism for enforcing limits on access to a resource in an environment where there are 
many threads of execution. A Lock has two states: locked and unlocked. If the state is locked, it does not allow other concurrent threads to
enter this code section until the state is unlocked again.
"""

from threading import Thread, Lock
import time

#Simulate a database
database_value = 0

def increase(lock):
    global database_value 
    
    #Lock the state before process
    lock.acquire()
    
    local_copy = database_value
    local_copy += 1
    time.sleep(0.1)
    database_value = local_copy
    
    #Unlock the state in the end
    lock.release()

#Locks with context manager
def decrease(lock):
    global database_value

    with lock:
        #Put your code here
        pass

    #Lock and unlocks safely

if __name__ == "__main__":

    #Create a lock object
    lock = Lock()
    
    print('Start value: ', database_value)

    #Pass the lock as an argument so it could be used in both Threads
    t1 = Thread(target=increase, args=(lock,)) #Notice the comma after 'lock' to make a tuple
    t2 = Thread(target=increase, args=(lock,))

    #Same as usual
    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

