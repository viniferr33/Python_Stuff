import functools

"""
##### Decorators #####

"""

# Syntax
###


@mydecorator         # This is a decorator, it will extend the functionality of the function/method bellow, it can return a value, process data or do anything
def myfunction():
    pass

# Example
###


def moo(func):                          # This will be a decorator, it takens a function as argument

    # The Wrapper will be returned, it will contains all the logic arround the given function
    def wrapper(*args, **kwargs):
        # The *args, **kwargs allows the function to accept any number of arguments, avoiding any needless creation of many decorators
        # This text will appear before the function
        print('sudo apt moo')
        func(*args, **kwargs)
        # This text will appear after the function
        print('moo')

    return wrapper


@moo
def have_u_mooed():
    print('have you mooed today?')


@moo
# This function have 1 more argument than the other, the *args, **kwargs makes the statement valid too
def the_number(x):
    print(f'The number is {x}')


# Identity
###

# Python assumes that the function affected by decorator is named 'wrapper'
def my_decorator(func):
    # To avoid this, you can use functools.wrap decorator
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        pass

    return wrapper

# Arguments
###


def repeat(qtd):                        # This will have a decorator with qtd argument

    def decorator_repeat(func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(qtd):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat


@repeat(4)                              # This will repeat 4 times
def cry():
    print('... crying ...')

# Class Decorators
###

class CallCounter:
    # Class decorators are useful when a attribute needs to be permantent e.g num_calls
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):            #This is the wrapper
        self.num_calls += 1
        print(f'Called {self.num_calls} times!')
        return self.func(*args, **kwargs)

@CallCounter
def idk():
    print('I dont Know')
