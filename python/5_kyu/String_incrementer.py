# Kata link:
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

# -------------------------------------
# Instructions:
'''
Your job is to write a function which increments a string, to create a new
string.

If the string already ends with a number, the number should be incremented
by 1.
If the string does not end with a number. The number 1 should be appended
to the new string.

Examples:

    foo -> foo1

    foobar23 -> foobar24

    foo0042 -> foo0043

    foo9 -> foo10

    foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''

# -------------------------------------
# Solution:
import re

def increment_string(strng):
    pattern = r'\d+$'
    numbers = re.findall(pattern, strng)
    if strng and numbers:
        num = str(int(numbers[0]) + 1).zfill(len(numbers[0]))
        return re.sub(pattern, num, strng)
    return strng + '1'


# -------------------------------------
# Basic Tests

print(increment_string("foo"), "foo1")
print(increment_string("foobar001"), "foobar002")
print(increment_string("foobar1"), "foobar2")
print(increment_string("foobar00"), "foobar01")
print(increment_string("foobar99"), "foobar100")
print(increment_string("foobar099"), "foobar100")
print(increment_string(""), "1")
