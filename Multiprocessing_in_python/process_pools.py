"""
##### Multiprocessing #####

    - Process Pools
"""

"""
## What is a Process Pool ##

A process pool object controls a pool of worker processes to which jobs can be submitted It supports asynchronous results with timeouts 
and callbacks and has a parallel map implementation. It can automatically manage the available processors and split data into smaller 
chunks which can then be processed in parallel by different processes.

## Important methods to use with Multiprocessing ##

    map(func, iterable[, chunksize]) : This method chops the iterable into a number of chunks which it submits to the process pool as separate 
    tasks. The (approximate) size of these chunks can be specified by setting chunksize to a positive integer. It blocks until the result is ready.

    close() : Prevents any more tasks from being submitted to the pool. Once all the tasks have been completed the worker processes will exit.

    join(): Wait for the worker processes to exit. One must call close() or terminate() before using join().

    apply(func, args): Call func with arguments args. It blocks until the result is ready. func is only executed in ONE of the workers of the pool.
"""


from multiprocessing import Pool 

def cube(number):
    return number * number * number

    
if __name__ == "__main__":
    numbers = range(10)
    
    p = Pool()

    #By default this allocates the maximum number of available processors for this task -> os.cpu_count()
    result = p.map(cube,  numbers)
    
    #Same as : result = [p.apply(cube, args=(i,)) for i in numbers]
    
    p.close()
    p.join()
    
    print(result)

