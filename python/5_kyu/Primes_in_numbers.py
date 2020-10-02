# Kata link:
# https://www.codewars.com/kata/54d512e62a5e54c96200019e

# -------------------------------------
# Instructions:
'''
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form :

		 "(p1**n1)(p2**n2)...(pk**nk)"
where a ** b means a to the power of b

with the p(i) in increasing order and n(i) empty if n(i) is 1.

Example:
		n = 86240 should return "(2**5)(5)(7**2)(11)"
'''

# -------------------------------------
# Solution:
def getAllPrimeFactors(n):
    """ A simple trial division """
    
    if (not isinstance(n, int)) or n <= 1:
        if n == 1:
            return [1]
        else:
            return []
    else:
        factors = []
        prime = 2
        while prime*prime <= n:
            while (n % prime) == 0:
                factors.append(prime)
                n //= prime
            prime += 1
        if n > 1:
            factors.append(n)
        return factors


def primeFactors(n):
    result = ""
    factors = getAllPrimeFactors(n)
    for i in sorted(set(factors)):
        count = factors.count(i)
        if count == 1:
            result += "({})".format(i)
        else:
            result += "({}**{})".format(i, count)
    return result




# -------------------------------------
# Basic Tests

print(primeFactors(86240) ==  "(2**5)(5)(7**2)(11)")
print(primeFactors(7775460) == "(2**2)(3**3)(5)(7)(11**2)(17)")
