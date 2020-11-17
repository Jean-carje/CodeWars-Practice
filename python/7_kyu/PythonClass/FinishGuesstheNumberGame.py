# kata:
# https://www.codewars.com/kata/568018a64f35f0c613000054/python

# -------------------------------------------------
# Solution:
class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
  
def guess(self,n):
        if n == self.number and self.lives > 0:
            return True
        elif n != self.number:
            self.lives -= 1
            return False
        else:
            raise 'Expect error: "Omae wa mo shindeiru"'

