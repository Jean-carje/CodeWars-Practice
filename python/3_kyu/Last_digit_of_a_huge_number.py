# Kata link:
# https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python

# -------------------------------------
# Solution:
def last_digit(lst):
    res = 1
    for n in reversed(lst):
        if res < 4:
            res = pow(n, res)
            continue
        res = pow(n, res % 4 + 4)
    return res % 10


# -------------------------------------
# Basic Tests

test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]
for test_input, test_output in test_data:
    print(last_digit(test_input) == test_output)
