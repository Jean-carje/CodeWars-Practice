# kata:
# https://www.codewars.com/kata/597c684822bc9388f600010f/train/python

# -------------------------------------------------
# Solution:
class Dinglemouse(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def get_full_name(self):
        name = self.first_name + ' ' + self.last_name
        return name.strip()
