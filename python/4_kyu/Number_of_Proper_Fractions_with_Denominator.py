# Kata link:
# https://www.codewars.com/kata/55b7bb74a0256d4467000070/train/python
# -------------------------------------
# Instructions:
'''
If n is the numerator and d the denominator of a fraction, that fraction is
defined a (reduced) proper fraction if and only if GCD(n,d)==1.

For example 5/16 is a proper fraction, while 6/16 is not, as both 6 and 16
are divisible by 2, thus the fraction can be reduced to 3/8.

Now, if you consider a given number d, how many proper fractions can be built
using d as a denominator?

For example, let's assume that d is 15: you can build a total of 8 different
proper fractions between 0 and 1 with it: 1/15, 2/15, 4/15, 7/15, 8/15, 11/15,
13/15 and 14/15.

You are to build a function that computes how many proper fractions you can
build with a given denominator:

proper_fractions(1)==0
proper_fractions(2)==1
proper_fractions(5)==4
proper_fractions(15)==8
proper_fractions(25)==20
Be ready to handle big numbers.
'''

# -------------------------------------
# Solution:

def proper_fractions(num):
    if num == 1:
        return 0
    x = num > 1 and num
    for p in range(2, int(num ** .5) + 1):
        if not num % p:
            x -= x // p
            while not num % p:
                num //= p
    if num > 1:
        x -= x // num
    return x


# -------------------------------------
# Basic Tests
print(proper_fractions(1),0)
print(proper_fractions(2),1)
print(proper_fractions(5),4)
print(proper_fractions(15),8)
print(proper_fractions(25),20)


