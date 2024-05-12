# -------------------------------------
# Solution:
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    list_n = []
    for i in range(1, n + 1):
        list_n.append(x * i)
        
    return list_n

