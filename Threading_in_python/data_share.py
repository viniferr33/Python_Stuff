"""
###### Threading ######

    - Data sharing
"""
from threading import Thread
import time

#Simulate a database
database_value = 0

def increase():
    global database_value
    
    #Simulate data retrieving
    local_copy = database_value
        
    #Simulate processing
    local_copy += 1
    time.sleep(0.1)
    
    #Write the calculated new value
    database_value = local_copy


if __name__ == "__main__":

    print('Start value: ', database_value)

    t1 = Thread(target=increase)
    t2 = Thread(target=increase)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print('End value:', database_value)

    print('end main')

    # Notice that end result will be:
    # Start value: 0
    # End value: 1

    """
    But why 'end value' isnt = 2?
    A race contition occured, which means that two or more threads access the same data in the same time.
    """