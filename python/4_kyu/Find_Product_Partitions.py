# Kata link:
# https://www.codewars.com/kata/571dd22c2b97f2ce400010d4/

# -------------------------------------
# Solution:
from itertools import permutations

def part(n):
    par = []
    prime = 2
    while prime * prime <= n:
        while n % prime == 0:
            par.append(prime)
            n //= prime
        prime += 1
    if n > 1:
        par.append(n)
    return par[::-1]

def numb(ar):
    res = {sum(tp ** ar.count(tp) for tp in set(ar)) * len(ar): ar}
    contr = 2
    while contr < len(ar):
        for i in permutations(ar, r=contr):
            nu = 1
            temp = ar[:]
            for j in i:
                nu *= j
                temp.remove(j)
            prod_part = [nu, * temp]
            prod_part.sort(reverse=True)
            score = 0
            for t in set(prod_part):
                score += t ** prod_part.count(t)
            score *= len(prod_part)
            res[score] = prod_part
        contr += 1
    return res

def find_spec_prod_part(n, com):
    partt = part(n)
    if len(partt) == 1:
        return "It is a prime number"

    result = numb(partt)
    elem = result.copy()
    for r, s in elem.items():
        for it, st in numb(s).items():
            result[it] = st
    if com == "max":
        maxP = max(result.keys())
        return [result[maxP], maxP]
    else:
        minP = min(result.keys())
        return [result[minP], minP]


