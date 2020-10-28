# Kata link:
# https://www.codewars.com/kata/556c04c72ee1147ff20000c9/solutions/python

# -------------------------------------
# -------------------------------------
# Solution:
from collections import Counter
from itertools import permutations

def valid(a):
    string = "".join(["".join(el) for el in a])

    p = Counter(string)

    if len(set(p.values())) > 1:
        return False

    comb = list(permutations(p.keys(), 2))
    for day in a:
        for group in day:
            team = list(permutations(list(group), 2))
            for t in team:
                try:
                    comb.remove(t)
                except:
                    return False
    return True


# -------------------------------------
# Basic Tests

import unittest


class Test(unittest.TestCase):
    """
    Positive Test: 1-3
    Negative Test: 4-5
    """

    def test_1(self):
        """can handle the two-player case"""
        s = [["AB"]]
        print("Four players, two days works")
        return self.assertEqual(valid(s), True)

    def test_2(self):
        """can handle a four-player case"""
        s = [
            ["AB", "CD"],
            ["AD", "BC"],
            ["BD", "AC"]]
        print("Four players, three days works")
        return self.assertEqual(valid(s), True)

    def test_3(self):
        """can handle the case from Wolfram MathWorld"""
        s = [
            ['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
            ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
            ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
            ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
        ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]
        print("Wolfram MathWorld case works")
        return self.assertEqual(valid(s), True)

    def test_4(self):
        """can detect days with different number of groups"""
        s = [
            ["AB", "CD", "EF", "GH"],
            ["AC", "BD", "EG", "FH"],
            ["AD", "CE"],
            ["AE", "BG", "CH", "FD"]]
        print("Must reject day with fewer groups")
        return self.assertEqual(valid(s), False)

    def test_5(self):
        """can detect two players appearing twice"""
        s = [
            ["ABC", "DEF"],
            ["ADE", "CBF"]]
        print("Must reject B & C playing together twice")
        return self.assertEqual(valid(s), False)


if __name__ == "__main__":
    unittest.main(verbosity=2)
