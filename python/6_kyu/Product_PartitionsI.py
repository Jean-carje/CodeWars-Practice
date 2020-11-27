# kata:
# https://www.codewars.com/kata/56135a61f8b29814340000cd/

# --------------------------------------------------
# Solution:
from itertools import permutations, combinations


def factor(x):
    p = 2
    res = []
    while p * p <= x:
        while x % p == 0:
            res.append(p)
            x //= p
        p += 1
    if x > 1:
        res.append(x)
    return res


# def prod_int_part(n):
    # result = [0, []]
    # f = factor(n)
    # if f == [n]:
        # return result
    # tp = 0
    # while len(f) > tp:
        # temp = f[:tp] + f[tp + 1:]
        # numb = 1
        # for i in temp:
            # numb *= i
        # l = sorted([f[tp], numb])
        # print(l)
        # if l not in result[1]:
            # result[1].append(l)
        # tp += 1
    # result[0] = len(result[1]) + 1
    # result[1] = f
    # return result

def prod_int_part(n):
    result = [0, []]
    f = factor(n)
    l = []
    for i in len(f):
        temp = []
        
    return l
# --------------------------------------------------
# Test:

print(factor(60))

# print(prod_int_part(18), [3, [2, 3, 3]])
print(prod_int_part(60), [10, [2, 2, 3, 5]])
# print(prod_int_part(54), [6, [2, 3, 3, 3]])
# print(prod_int_part(37), [0, []])
# print(prod_int_part(61), [0, []])



