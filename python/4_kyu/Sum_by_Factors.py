# Kata link:
# https://www.codewars.com/kata/54d496788776e49e6b00052f/

# -------------------------------------
# Solution:

def factors(n):
    factorsNumbers = []
    prime = 2
    while prime * prime <= n:
        while (n % prime == 0):
            factorsNumbers.append(prime)
            n //= prime
        prime += 1
    if n > 1:
        factorsNumbers.append(n)
    return set(factorsNumbers)

def sum_for_list(lst):
    mp = {}
    for i in lst:
        for j in factors(abs(i)):
            if not mp.get(j):
                mp.setdefault(j, i)
                continue
            mp[j] += i
    return sorted(list(el) for el in mp.items())

# # -------------------------------------

