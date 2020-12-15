"""
###### Multiprocessing ######

    - Creating various Process
"""

#Create and run
from multiprocessing import Process
import os

"""
process = multiprocessing.Process(target=, args=)

target -> Is a callable object for this process
args -> the function arguments, must be a tuple.
"""

def square_numbers():
    for i in range(1000):
        result = i * i
        
if __name__ == "__main__":        
    processes = []

    #Number of CPUs on the machine. Usually is a good choise for the number of processes
    num_processes = os.cpu_count()

    #Create a process and asign a function for each
    for i in range(num_processes):
        process = Process(target=square_numbers)
        processes.append(process)

    #Start all processes
    for process in processes:
        process.start()

    #Wait for all processes to finish
    #Block the main programm until these processes are finished
    for process in processes:
        process.join()