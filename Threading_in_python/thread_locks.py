"""
###### Threading ######

    - Data Locks
"""

"""
Avoid race contitions

Because the thread scheduling, algorithm can swap between threads at any time, you don't know the order in which the threads will attempt to access the shared data. In our case, the first thread accesses the database_value (0) and stores it in a local copy. It then increments it (local_copy is now 1). With our time.sleep() function that just simulates some time consuming operations, the programm will swap to the second thread in the meantime. This will also retrieve the current database_value (still 0) and increment the local_copy to 1. Now both threads have a local copy with value 1, so both will write the 1 into the global database_value. This is why the end value is 1 and not 2.
"""
