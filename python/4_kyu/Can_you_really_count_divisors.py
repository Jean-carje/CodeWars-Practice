# https://www.codewars.com/kata/58b16300a470d47498000811/train/python

def count_divisors(n):
    total = 1
    for i in range(2, n + 1):
        # print(n // i)
        if n % i == 0:
            total += i
    return total

# =================================================================
# # test
print(count_divisors(5))
print(count_divisors(10))
print(count_divisors(5) == 10)
print(count_divisors(10) == 27)
