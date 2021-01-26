# Kata link:
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/

# -------------------------------------
# Solution:
def move_zeros(array):
    ar = []
    for i in array:
        if type(i) is int or type(i) is float:
            if -1 < i < 1:
                continue
        ar.append(i)
    for _ in range(len(array) - len(ar)):
        ar.append(0)
    return ar

