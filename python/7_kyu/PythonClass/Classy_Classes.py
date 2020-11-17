# kata:
# https://www.codewars.com/kata/55a144eff5124e546400005a/train/python

# -------------------------------------------------
# Solution:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
