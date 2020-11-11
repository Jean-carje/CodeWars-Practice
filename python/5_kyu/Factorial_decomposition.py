# Kata link:
# https://www.codewars.com/kata/5a045fee46d843effa000070

# -------------------------------------
# -------------------------------------
# Solution:

def primes(n):
    """
    return all primes number of n
    """
    p = 2
    res = []
    while p * p <= n:
        while n % p == 0:
            res.append(p)
            n //= p
        p += 1
    if n > 1:
        res.append(n)
    return res


def decomp(n):
    fctrs = {}
    result = ""

    while n > 1:
        tp = primes(n)
        n -= 1
        for i in set(tp):
            if i in fctrs:
                fctrs[i] += tp.count(i)
            else:
                fctrs[i] = tp.count(i)

    fctrs = sorted(fctrs.items(), key=lambda x: x[1])
    fctrs.reverse()

    for i in fctrs:
        if i[1] == 1:
            result += f"{i[0]}"
        else:
            result += f"{i[0]}^{i[1]}"

        if i != fctrs[-1]:
            result += " * "

    return result


# -------------------------------------
# Test

print(decomp(5) == "2^3 * 3 * 5")
print(decomp(14) == "2^11 * 3^5 * 5^2 * 7^2 * 11 * 13")
print(decomp(17) == "2^15 * 3^6 * 5^3 * 7^2 * 11 * 13 * 17")
print(decomp(22) == "2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19")
print(decomp(25) == "2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23")
print(decomp(79) == "2^74 * 3^36 * 5^18 * 7^12 * 11^7 * 13^6 * 17^4 * 19^4 * 23^3 * 29^2 * 31^2 * 37^2 * 41 * 43 * 47 * 53 * 59 * 61 * 67 * 71 * 73 * 79")

