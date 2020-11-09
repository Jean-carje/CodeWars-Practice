# Kata link:
# https://www.codewars.com/kata/55cf3b567fc0e02b0b00000b/

# -------------------------------------
# Solution:
from statistics import median

def partInArray(n):
    """
    partition
    """
    part = []
    p = [0] * n
    k = 0
    p[k] = n

    while True:
        part.append([p[i] for i in range(0, k + 1)])
        val = 0

        while k >= 0 and p[k] == 1:
            val += p[k]
            k -= 1
        
        if k < 0:
            return part

        p[k] -= 1
        val += 1

        while val > p[k]:
            p[k + 1] = p[k]
            val = val - p[k]
            k += 1

        p[k + 1] = val
        k += 1


def part(n):

    partition = partInArray(n)

    prod = set()
    for numb in partition:
        tmp = 1
        for j in numb:
            tmp *= j
        prod.add(tmp)
    prod = list(prod)
    rang = max(prod) - min(prod)
    average = sum(prod) / len(prod)
    media = median(prod)

    return "Range: {} Average: {:0.2f} Median: {:0.2f}".format(rang, average, media)


# -------------------------------------
# Basic Tests
print(part(1) == "Range: 0 Average: 1.00 Median: 1.00")
print(part(2) == "Range: 1 Average: 1.50 Median: 1.50")
print(part(3) == "Range: 2 Average: 2.00 Median: 2.00")
print(part(4) == "Range: 3 Average: 2.50 Median: 2.50")
print(part(5) == "Range: 5 Average: 3.50 Median: 3.50")

