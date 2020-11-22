"""
##### Errors and Exceptions #####

    *Raise                  ->  Force an exception when a certain condition occur
    *Try and Except         ->  Catch exceptions without stop the program
    *Custom Exceptions      ->  Creating your exceptions
    
"""

### Raise
###
x = 11
if x < 10:
    raise Exception(f'The given number needs to be greater than 10!')

### Try and Except
###
try:
    a = 0/0
    b = 10 + '10'

except ZeroDivisionError as e:
    print('Imagine that you have zero cookies 🍪, and you split them evenly among zero friends.\nHow many cookies does each person get? See? It doesn’t make sense.\nAnd Cookie Monster is sad that there are no cookies, and you are sad that you have no friends. 😢')

except TypeError as e:
    print('Trying to add a character to a number? lol')

else:
    print('Moo')    #It runs if there are no exceptions

finally:
    print('Everything is fine!')

### Custom Exceptions
###
class TooHigh(Exception):
    pass

y = 50*50
if y > 1000:
    raise TooHigh('The value is too High!')

