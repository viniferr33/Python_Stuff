"""
###### Threading ######

    - Creating Threads
"""

#Create and run
from threading import Thread
"""
thread = threading.Thread(target, (arg1, arg2, arg3))

target -> Is a callable object for this thread
args -> the function arguments, must be a tuple.
"""

def square_number():
    for i in range(1000):
        result = i * i

if __name__ == "__main__":
    threads = []
    num_threads = 10

    #Create a thread and asign a function for each
    for i in range(num_threads):
        thread = Thread(target=square_number)
        threads.append(thread)

    #Start all threads
    for thread in threads:
        thread.start()

    #Wait for all threads to finish
    #Block the main thread until these threads are finished
    for thread in threads:
        thread.join()