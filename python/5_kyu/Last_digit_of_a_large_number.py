# Kata link:
# https://www.codewars.com/kata/5511b2f550906349a70004e1/

# -------------------------------------
# Solution:

def last_digit(a, b):
    return pow(a, b, 10)


print(last_digit(4, 1), 4)
print(last_digit(4, 2), 6)
print(last_digit(9, 7), 9)
print(last_digit(10, 10 ** 10), 0)
print(last_digit(2 ** 200, 2 ** 300), 6)
