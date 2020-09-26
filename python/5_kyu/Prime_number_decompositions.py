# Kata link:
# https://www.codewars.com/kata/53c93982689f84e321000d62/

# -------------------------------------
# Instructions:
'''
You have to code a function getAllPrimeFactors wich take an integer
as parameter and return an array containing its prime decomposition
by ascending factors, if a factors appears multiple time in the
decomposition it should appear as many time in the array.

	exemple: getAllPrimeFactors(100) returns [2,2,5,5] in this order.

This decomposition may not be the most practical.

You should also write getUniquePrimeFactorsWithCount, a function
which will return an array containing two arrays: one with prime
numbers appearing in the decomposition and the other containing
their respective power.

	exemple: getUniquePrimeFactorsWithCount(100) returns [[2,5],[2,2]]

You should also write getUniquePrimeFactorsWithProducts an array
containing the prime factors to their respective powers.

	exemple: getUniquePrimeFactorsWithProducts(100) returns [4,25]

Errors, if:

	n is not a number
	n not an integer
	n is negative or 0
	The three functions should respectively return [], [[],[]] and [].

Edge cases:

	if n=0, the function should respectively return [], [[],[]] and [].
	if n=1, the function should respectively return [1], [[1],[1]], [1].
	if n=2, the function should respectively return [2], [[2],[1]], [2].

The result for n=2 is normal. The result for n=1 is arbitrary and has
been chosen to return a usefull result. The result for n=0 is also
arbitrary but can not be chosen to be both usefull and intuitive. 
([[0],[0]] would be meaningfull but wont work for general use of
decomposition, [[0],[1]] would work but is not intuitive.)
'''

# -------------------------------------
# Solution:

def getAllPrimeFactors(n):
	""" A simple trial division
	"""
	if type(n) != int or n <= 1:
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

def getUniquePrimeFactorsWithCount(n):
	if type(n) != int or n <= 1:
		if n == 1:
			return [[1],[1]]
		else:
			return [[],[]]
	else:
		factors = getAllPrimeFactors(n)
		primeNumbers = [[],[]]
		for i in set(factors):
			primeNumbers[0].append(i)
			primeNumbers[1].append(factors.count(i))
		return primeNumbers

def getUniquePrimeFactorsWithProducts(n):
	if type(n) != int or n <= 1:
		if n == 1:
			return [1]
		else:
			return []
	else:
		primeNumbers = getUniquePrimeFactorsWithCount(n)
		result = []
		for i in zip(primeNumbers[0], primeNumbers[1]):
			result.append(i[0] ** i[1])
		return result

# -------------------------------------
# Basic Tests
print('Test 1')
print(getAllPrimeFactors(100), [2,2,5,5])
print(getUniquePrimeFactorsWithCount(100), [[2,5],[2,2]])
print(getUniquePrimeFactorsWithProducts(100), [4,25])

print('Test 2')
print(getAllPrimeFactors(0))
print(getUniquePrimeFactorsWithCount(0))
print(getUniquePrimeFactorsWithProducts(0))

print('Test 3')
print(getAllPrimeFactors(1))
print(getUniquePrimeFactorsWithCount(1))
print(getUniquePrimeFactorsWithProducts(1))

print('Test 4')
print(getAllPrimeFactors(2))
print(getUniquePrimeFactorsWithCount(2))
print(getUniquePrimeFactorsWithProducts(2))