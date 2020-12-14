# Kata link:
# https://www.codewars.com/kata/513fa1d75e4297ba38000003

# -------------------------------------
# Solution:
# from collections.abc import Iterable

# def temp(x):
    # for t in x:
        # if isinstance(t, Iterable) and not isinstance(t, (str, bytes)):
            # yield from flatten(t)
        # else:
            # yield t

def flatten(*args):
    res = []
    for item in args:
        if isinstance(item, list):
            res.extend(flatten(*item))
        else:
            res.append(item)
    return res


