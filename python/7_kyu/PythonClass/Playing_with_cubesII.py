# kata:
# https://www.codewars.com/kata/55c0ac142326fdf18d0000af/train/python

# -------------------------------------------------
# Solution:
class Cube(object):
    def __init__(self, side=0):
        self._side = side
    
    def get_side(self):
        """Return the side of the Cube"""
        return abs(self._side)

    def set_side(self, new_side):
        """Set the value of the Cube's side."""
        self._side = new_side
