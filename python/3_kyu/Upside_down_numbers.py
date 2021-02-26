# Kata link:
# https://www.codewars.com/kata/59f7597716049833200001eb/

# -------------------------------------
# Solution:
def check(num):
    combinations = ["00","11","88","69","96"]
    i = 0
    j = len(num) - 1
    while i <= j:
        n = num[i] + num[j]
        if not n in combinations:
            return False
        i += 1
        j -= 1
    return True

def solve(a, b):
    cont = 0
    for n in range(a, b):
        if check(str(n)):
            cont += 1
    return cont


# -------------------------------------
# Basic Tests
print(solve(0,10),3)
print(solve(10,100),4)
print(solve(1000,10000),20)
print(solve(10000,15000),6)
print(solve(15000,20000),9)
print(solve(60000,70000),15)
print(solve(60000,130000),55)
