# Kata link:
# https://www.codewars.com/kata/568f2d5762282da21d000011/train/python

# -------------------------------------
# Solution:
import itertools

def gta(limit, *args):
    gta_value = 0
    new = []
    for i in itertools.zip_longest(*[str(i) for i in args]):
        for n in i:
            if n != None and int(n) not in new:
                new.append(int(n))
    for contr in range(limit + 1):
        for numb in itertools.permutations(new[:limit], contr):
            gta_value += sum(numb)

    return gta_value

# -------------------------------------
# Basic Tests
print(gta(7, 123489, 5, 67), 328804) 

print(gta(8, 12348, 47, 3639), 3836040)

