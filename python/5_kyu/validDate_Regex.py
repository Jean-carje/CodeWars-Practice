# Kata link:
# https://www.codewars.com/kata/548db0bd1df5bbf29b0000b7

# -------------------------------------
# Instructions:
'''
Write a regular expression (regex) that will match a string only if it
contains at least one valid date, in the format [mm-dd] (that is, a two-digit
month, followed by a dash, followed by a two-digit date, surrounded by square
brackets).

For example:

    "[01-23]" // January 23rd is a valid date
    "[02-31]" // February 31st is an invalid date
    "[02-16]" // valid
    "[ 6-03]" // invalid format
    "ignored [08-11] ignored" // valid
    "[3] [12-04] [09-tenth]" // December 4th is a valid date
'''

# -------------------------------------
# Solution:

import re

valid_date = re.compile(r"""^.*\[
                        (
                        (02-(0[1-9]|1[0-9]|2[0-8]))|
                        (04|06|09|11)-(0[1-9]|1[0-9]|2[0-9]|30)|
                        (01|03|05|07|08|10|12)-(0[1-9]|1[0-9]|2[0-9]|3[01]))
                        (?:\]).*$""")

# -------------------------------------
# Basic Tests

print("Basic tests")
print(valid_date.search("[01-23]") != None, "January 23rd is a valid date")
print(valid_date.search("[02-31]") == None, "February 31st is an invalid date")
print(valid_date.search("[02-16]") != None, "valid")
print(valid_date.search("[ 6-03]") == None, "invalid format")
print(valid_date.search("ignored [08-11] ignored") != None, "valid")
print(valid_date.search("[3] [12-04] [09-tenth]") != None, "December 4th is a valid date")
print(valid_date.search("[02-00]") == None, "invalid format")
print(valid_date.search("[[[08-29]]]") != None, "valid")
print(valid_date.search("[13-02]") == None, "invalid format")
print(valid_date.search("[02-[08-11]04]") != None, "valid")
