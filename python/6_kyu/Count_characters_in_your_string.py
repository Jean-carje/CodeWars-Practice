# kata:
# https://www.codewars.com/kata/52efefcbcdf57161d4000091/

# --------------------------------------------------
# Solution 1:
# def count(string):
    # res = {}
    # for i in sorted({w: string.count(w) for w in set(string)}.items(), key=lambda x: x[0]):
        # res[i[0]] = i[1]
    # return res

# Solution 2:
from collections import Counter 

def count(string):
    return dict(Counter(string))

# --------------------------------------------------


