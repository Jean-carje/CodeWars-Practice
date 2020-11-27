# kata:
# https://www.codewars.com/kata/56135a61f8b29814340000cd/

# --------------------------------------------------
# Solution:
# Failed: 10

from itertools import combinations
from math import prod

# def prod(arr):
    # result = 1
    # for i in arr:
        # result *= i
    # return result

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



def partitions(n):
    result = []
    f = factor(n)
    for i in range(len(f)):
        l = f.copy()
        del l[i]
        result.append([f[i], prod(l)])
        if i < len(f) - 1:
            numb = f[i] * l.pop(0)
            result.append([numb, prod(l)])
    result = sorted(set(map(tuple, result)))
    return result



def prod_int_part(n):
    result = [0, []]
    c = []
    f = factor(n)
    if n in f:
        return result
    for el in partitions(n):
        a = factor(el[0])
        b = factor(el[1])
        if sorted(el) not in c:
            c.append(sorted(el))
        if len(a) > 1:
            res = sorted([*a, el[1]])
            if res not in c:
                c.append(res)
                continue
        for i in range(2, len(f) + 1):
            for n in combinations(b, i):
                if prod(n) == el[1]:
                    res = sorted([el[0], *n])
                    for d in partitions(el[1]):
                        tp = sorted([el[0], *d])
                        if tp not in c and 1 not in tp:
                            c.append(tp)
                    if res not in c:
                        c.append(res)
                        continue
    result[0] = len(c)
    result[1] = c[1]
    for i in c:
        if 1 in i:
            del i[0]
        if len(i) > len(c[1]):
            result[1] = i
    return result
        

# --------------------------------------------------
# Test:
print(prod_int_part(18), [3, [2, 3, 3]])
print(prod_int_part(60), [10, [2, 2, 3, 5]])
print(prod_int_part(54), [6, [2, 3, 3, 3]])
print(prod_int_part(37), [0, []])
print(prod_int_part(61), [0, []])



