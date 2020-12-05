# kata:
# https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

# --------------------------------------------------
# Solution:
from collections import Counter


def duplicate_count(text):
    """With collections.Counter()"""
    result = 0
    count = Counter(text.lower())
    for i in count:
        if count.get(i) > 1:
            result += 1
    return result

# def duplicate_count(text):
    # """Without collections.Counter()"""
    # result = 0
    # text = text.lower()
    # for i in set(text.lower()):
        # if text.count(i) > 1:
            # result += 1
    # return result


# --------------------------------------------------

print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdea"), 1)
print(duplicate_count("indivisibility"), 1)
print(duplicate_count("Indivisibilities"), 2)

