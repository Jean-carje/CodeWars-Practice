# kata:
# https://www.codewars.com/kata/55a14aa4817efe41c20000bc/python

# -------------------------------------------------
# Solution:
class Cat(Animal):
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return f"{self.name} meows."
