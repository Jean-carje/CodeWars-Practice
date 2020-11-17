# kata:
# https://www.codewars.com/kata/52adc142b2651f25a8000643/

# -------------------------------------------------
# Solution:

class Sleigh(object):
    def authenticate(self, name, password):
        self.name = name
        self.password = password
        return self.name == "Santa Claus" and self.password == "Ho Ho Ho!"
