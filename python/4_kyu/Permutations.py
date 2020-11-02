# Kata link:
# https://www.codewars.com/kata/5254ca2719453dcc0b00027d/

# -------------------------------------
# Solution:
import itertools

def permutations(string):
    return [*set("".join(i) for i in (d for d in itertools.permutations(string)))]

# -------------------------------------
# Basic Tests
print(sorted(permutations('a')) == ['a'])

print(sorted(permutations('ab')) == ['ab', 'ba'])

print(sorted(permutations('aabb')) == ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])

