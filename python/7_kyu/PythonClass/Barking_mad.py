# kata:
# https://www.codewars.com/kata/54dba07f03e88a4cec000caf/

# -------------------------------------------------
# Solution:
class Dog ():
    def __init__(self, breed):
        self.breed = breed
    
    def bark(self):
        return "Woof"

snoopy = Dog("Beagle")

snoopy.bark = lambda: "Woof"

scoobydoo = Dog("Great Dane")
