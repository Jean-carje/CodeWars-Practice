# kata:
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

# --------------------------------------------------
# Solution:
def unique_in_order(iterable):
    res = []
    if iterable:
        res.append(iterable[0])
        for i in iterable:
            if res[-1] != i:
                res.append(i)
    return res


# --------------------------------------------------



print(unique_in_order('AAAABBBCCDAABBB'), ['A','B','C','D','A','B'])


