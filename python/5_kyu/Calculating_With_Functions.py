# Kata link:
# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

# -------------------------------------
# Instructions:
'''
This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3

Requirements:

- There must be a function for each number from 0 ("zero") to 9 ("nine")
- There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
- Each calculation consist of exactly one operation and two numbers
- The most outer function represents the left operand, the most inner function represents the right operand
- Divison should be integer division. For example, this should return 2, not 2.666666...:

eight(divided_by(three()))
'''

def zero(op = None):
    if op == None:
        return 0
    else:
        return op(0)
def one(op = None):
    if op == None:
        return 1
    else:
        return op(1)
def two(op = None):
    if op == None:
        return 2
    else:
        return op(2)
def three(op = None):
    if op == None:
        return 3
    else:
        return op(3)
def four(op = None):
    if op == None:
        return 4
    else:
        return op(4)
def five(op = None):
    if op == None:
        return 5
    else:
        return op(5)
def six(op = None):
    if op == None:
        return 6
    else:
        return op(6)
def seven(op = None):
    if op == None:
        return 7
    else:
        return op(7)
def eight(op = None):
    if op == None:
        return 8
    else:
        return op(8)
def nine(op = None):
    if op == None:
        return 9
    else:
        return op(9)

def plus(numb):
    return lambda x: x + numb
def minus(numb):
    return lambda x: x - numb
def times(numb):
    return lambda x: x * numb
def divided_by(numb):
    return lambda x: x // numb


# Basic Tests
print(seven(times(five())),"=", 35)
print(four(plus(nine())),"=", 13)
print(eight(minus(three())),"=", 5)
print(six(divided_by(two())),"=", 3)