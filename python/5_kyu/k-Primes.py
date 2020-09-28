# Kata link:
# https://www.codewars.com/kata/5726f813c8dcebf5ed000a6b/

# -------------------------------------
# Instructions:
'''
A natural number is called k-prime if it has exactly k prime factors,
counted with multiplicity. For example:

	k = 2  -->  4, 6, 9, 10, 14, 15, 21, 22, ...
	k = 3  -->  8, 12, 18, 20, 27, 28, 30, ...
	k = 5  -->  32, 48, 72, 80, 108, 112, ...
	A natural number is thus prime if and only if it is 1-prime.

Task:
Complete the function count_Kprimes (or countKprimes, count-K-primes, 
kPrimes) which is given parameters k, start, end (or nd) and returns 
an array (or a list or a string depending on the language - see "Solution"
and "Sample Tests") of the k-primes between start (inclusive) and end 
(inclusive).

Example:
	countKprimes(5, 500, 600) --> [500, 520, 552, 567, 588, 592, 594]
	
Notes:

The first function would have been better named: findKprimes or kPrimes :-)
In C some helper functions are given (see declarations in 'Solution').
For Go: nil slice is expected when there are no k-primes between start and end.

Second Task (puzzle):
Given a positive integer s, find the total number of solutions of the 
equation a + b + c = s, where a is 1-prime, b is 3-prime, and c is 7-prime.

Call this function puzzle(s).

Examples:
	puzzle(138)  -->  1  because [2 + 8 + 128] is the only solution
	puzzle(143)  -->  2  because [3 + 12 + 128] and [7 + 8 + 128] are the solutions
'''

# -------------------------------------
# Solution:
def factors(n):
	""" A simple trial division
	"""
	prime_factors = 0 
	prime = 2
	while prime*prime <= n:
		while (n % prime) == 0:
			prime_factors += 1
			n //= prime
		prime += 1
	if n > 1:
		prime_factors += 1
	return prime_factors

def count_Kprimes(k, start, nd):
	result = []
	for i in range(start, nd+1):
		if factors(i) == k:
			result.append(i)
	return result

def puzzle(s):
	a = count_Kprimes(1, 0, s)
	b = count_Kprimes(3, 0, s)
	c = count_Kprimes(7, 0, s)

	return sum(1 for x in a for y in b for z in c if x + y + z == s)


# -------------------------------------
# Basic Tests

print('Test count_Kprimes:')

print('1:', count_Kprimes(2, 0, 100) == [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82, 85, 86, 87, 91, 93, 94, 95])

print('2:', count_Kprimes(3, 0, 100) == [8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99])

print('3:', count_Kprimes(5, 1000, 1100) == [1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100])

print('4:', count_Kprimes(5, 500, 600) == [500, 520, 552, 567, 588, 592, 594])


print('\nTest puzzle:')
print('1:', puzzle(143) == 2)
print('2:', puzzle(138) == 1)

