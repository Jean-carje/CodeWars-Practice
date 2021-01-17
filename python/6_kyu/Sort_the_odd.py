# kata:
# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/

# --------------------------------------------------
# Solution:
def sort_array(source_array):
    arr = [n for n in sorted(source_array) if n % 2 != 0 and n != 0]
    for i, el in enumerate(source_array):
        if el % 2 == 0:
            arr.insert(i, el)
        elif el == 0:
            arr.append(el)
    return arr

# --------------------------------------------------
print(sort_array([5, 3, 2, 8, 1, 4]), [1, 3, 2, 8, 5, 4])
print(sort_array([5, 3, 1, 8, 0]), [1, 3, 5, 8, 0])
print(sort_array([]),[])


