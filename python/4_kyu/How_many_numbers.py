# Kata link:
# https://www.codewars.com/kata/5877e7d568909e5ff90017e6/

# -------------------------------------
# Solution:
from itertools import combinations_with_replacement


def find_all(sum_dig, digs):
    ttl = 0
    all_numbers = []
    for el in combinations_with_replacement(range(1, 10), digs):
        temp = ''
        if sum(el) == sum_dig:
            ttl += 1
            for i in sorted(el):
                temp += str(i)
            all_numbers.append(int(temp))
    return [ttl, min(all_numbers), max(all_numbers)] if all_numbers else []


