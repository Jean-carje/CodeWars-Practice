# Kata link:
# https://www.codewars.com/kata/54d496788776e49e6b00052f/

# -------------------------------------
# Instructions:
'''
Given an array of positive or negative integers

I= [i1,..,in]

you have to produce a sorted array P of the form

[ [p, sum of all ij of I for which p is a prime factor (p positive) of ij] ...]

P will be sorted by increasing order of the prime numbers. The final result has to be given as a string in Java, C#, C, C++ and as an array of arrays in other languages.

Example:

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
[2, 3, 5] is the list of all prime factors of the elements of I, hence the result.

Notes:

It can happen that a sum is 0 if some numbers are negative!
Example: I = [15, 30, -45] 5 divides 15, 30 and (-45) so 5 appears in the result, the sum of the numbers for which 5 is a factor is 0 so we have [5, 0] in the result amongst others.

In Fortran - as in any other language - the returned string is not permitted to contain any redundant trailing whitespace: you can use dynamically allocated character strings.
'''

# -------------------------------------
# Solution:
# Note: Don't work in all test

def sum_for_list(lst):
    def simple_abs(num):
        return -num if num < 0 else num
    abs_value_lst = []
    for i in lst:
        value = simple_abs(i)
        abs_value_lst.append(value)
    largest = max(abs_value_lst)
    
    p = []
    count = 2
    
    while count < largest:
        isprime = True
        for x in range(2, int((count/2) + 1)):
            if count % x == 0: 
                isprime = False
                break
        if isprime:
            p.append(count)
        count += 1
        
    sum_list = []
    sum = 0
    counter = 0
    
    for j in p:
        sum = 0
        counter = 0
        for i in lst:
            if not i % j:
                sum += i
                counter += 1
        if counter:
            sum_list.append([j, sum])
    return sum_list

# -------------------------------------
# Basic Tests:

a = [12, 15]
print(sum_for_list(a), '=', [[2, 12], [3, 27], [5, 15]])
