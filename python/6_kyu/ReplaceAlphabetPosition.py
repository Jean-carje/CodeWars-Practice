# kata:
# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

# --------------------------------------------------
# Solution:
from string import ascii_lowercase as lett

def alphabet_position(text):
    return " ".join((str(lett.find(i) + 1) for i in text.lower() if i in lett))


# --------------------------------------------------



print(alphabet_position("The sunset sets at twelve o' clock."))


