# Kata link:
# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

# -------------------------------------
# Solution:
def open_or_senior(data):
    return ['Senior' if i[0] >= 55 and i[1] > 7 else 'Open' for i in data]
