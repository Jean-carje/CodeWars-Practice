# Kata link:
# https://www.codewars.com/kata/59ccf051dcc4050f7800008f/train/python

# -------------------------------------
# -------------------------------------
# Solution:

def s(x):
    t = []
    for p in ([i, x//i] for i in range(1, int(x**0.5)+1) if not x % i):
        for n in p:
            t.append(n)
    return sum(set(t)) - x


def buddy(start, limit):
    for n in range(start,limit):
        t_m = n + 1
        t_n = s(n)
        m = t_n - 1

        if(m < start):
            continue

        if(s(m) == t_m):
            return [n,m]
    
    return 'Nothing'


# -------------------------------------
# Test
import unittest

class Test(unittest.TestCase):
    def test1(self):
        return self.assertEqual(buddy(10, 50), [48, 75])

    def test2(self):
        return self.assertEqual(buddy(2177, 4357), "Nothing")

    def test3(self):
        return self.assertEqual(buddy(57345, 90061), [62744, 75495])

    def test4(self):
        return self.assertEqual(buddy(1071625, 1103735), [1081184, 1331967])


if __name__ == '__main__':
    unittest.main(verbosity=2)
