# Kata link:
# https://www.codewars.com/kata/52e1476c8147a7547a000811

# -------------------------------------
# Instructions:
'''
You need to write regex that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.

'''
# -------------------------------------
# Solution:

regex="^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[a-zA-Z\d]{6,}$"


# -------------------------------------
# Basic Tests
from re import search
print(bool(search(regex, 'fjd3IR9')), True)
print(bool(search(regex, 'ghdfj32')), False)
print(bool(search(regex, 'DSJKHD23')), False)
print(bool(search(regex, 'dsF43')), False)
print(bool(search(regex, '4fdg5Fj3')), True)
print(bool(search(regex, 'DHSJdhjsU')), False)
print(bool(search(regex, 'fjd3IR9.;')), False)
print(bool(search(regex, 'fjd3  IR9')), False)
print(bool(search(regex, 'djI38D55')), True)
print(bool(search(regex, 'a2.d412')), False)
print(bool(search(regex, 'JHD5FJ53')), False)
print(bool(search(regex, '!fdjn345')), False)
print(bool(search(regex, 'jfkdfj3j')), False)
print(bool(search(regex, '123')), False)
print(bool(search(regex, 'abc')), False)
print(bool(search(regex, '123abcABC')), True)
print(bool(search(regex, 'ABC123abc')), True)
print(bool(search(regex, 'Password123')), True)