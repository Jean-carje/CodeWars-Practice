# Kata link:
# https://www.codewars.com/kata/53efc28911c36ff01e00012c

# -------------------------------------
# Instructions:
'''
The aim of this kata is to determine the number of sub-function calls made by
an unknown function.

You have to write a function named count_calls which:

    takes as parameter a function and its arguments (args, kwargs)

    calls the function

    returns a tuple containing:

        the number of function calls made inside it and inside all the
            sub-called functions recursively
        the function return value.
NB: The call to the function itself is not counted.

HINT: The sys module may come in handy.
'''

# -------------------------------------
# Solution:
import sys


def count_calls(func, *args, **kwargs):
    """
    Count calls in function func
    """
    calls = [-1]
    def tracer(frame, event, arg):
        if event == 'call':
            calls[0] += 1
        return tracer

    sys.settrace(tracer)

    rv = func(*args, **kwargs)
    return calls[0], rv


# -------------------------------------
# Basic Tests


def add(a, b):
    return a + b


def add_ten(a):
    return add(a, 10)


def misc_fun():
    return add(add_ten(3), add_ten(9))


print(count_calls(add, 8, 12) == (0, 20))
print(count_calls(add_ten, 5) == (1, 15))
print(count_calls(misc_fun) == (5, 32))
