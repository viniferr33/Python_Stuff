"""
###### Multiprocessing ######

    - Data Locks
"""

"""
## Avoid race contitions ##

A race condition happened here. A race condition occurs when two or more processes or threads can access shared data and they try to change 
it at the same time. In our example the two processes have to read the shared value, increase it by 1, and write it back into the shared 
variable. If this happens at the same time, the two processes read the same value, increase it and write it back. Thus, both processes write 
the same increased value back into the shared object, and the value was not increased by 2.

## Locks ##

A lock (also known as mutex) is a synchronization mechanism for enforcing limits on access to a resource in an environment where there are 
many processes of execution. A Lock has two states: locked and unlocked. If the state is locked, it does not allow other concurrent processes 
to enter this code section until the state is unlocked again.
"""

from multiprocessing import Process, Value, Array, Lock
import time

def add_100(number, lock):
    for _ in range(100):
        time.sleep(0.01)
    
        #Lock the state before process
        lock.acquire()
        
        number.value += 1
        
        #Unlock the state in the end
        lock.release()

def add_100_array(numbers, lock):
    for _ in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            #Lock the state before process
            lock.acquire()
            numbers[i] += 1

            #Unlock the state in the end
            lock.release()


if __name__ == "__main__":

    #Create a lock object
    lock = Lock()
    
    shared_number = Value('i', 0) 
    print('Value at beginning:', shared_number.value)

    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at beginning:', shared_array[:])

    #Pass the lock as an argument so it could be used in both Threads
    process1 = Process(target=add_100, args=(shared_number, lock))
    process2 = Process(target=add_100, args=(shared_number, lock))
    process3 = Process(target=add_100_array, args=(shared_array, lock))
    process4 = Process(target=add_100_array, args=(shared_array, lock))

    #Same as usual
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