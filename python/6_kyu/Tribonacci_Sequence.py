# kata:
# https://www.codewars.com/kata/556deca17c58da83c00002db/

# --------------------------------------------------
# Solution:

def tribonacci(signature, n):
    result = signature[:n]
    for _ in range(n - len(signature)):
        result.append(sum(result[-3:]))
    return result


