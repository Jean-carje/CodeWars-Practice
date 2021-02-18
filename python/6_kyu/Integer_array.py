# kata:
# https://www.codewars.com/kata/52a112d9488f506ae7000b95/train/python

# --------------------------------------------------
def is_int_array(arr):
    flag = isinstance(arr, list)
    if arr:
        for i in arr:
            if isinstance(i, float):
                flag = i.is_integer()
            elif not isinstance(i, int):
                    return False
    return flag

# --------------------------------------------------


