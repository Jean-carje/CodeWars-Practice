# Kata:
# https://www.codewars.com/kata/51f42b1de8f176db5a0002ae/

# ---------------------------------------------------
# Solution 1:

def sort_me(courses):
    temp = [(i.split('-')[1], i.split('-')[0]) for i in courses]
    result = [n[1] + '-' + str(n[0]) for n in sorted(temp)]
    return result

# ---------------------------------------------------
# Solution 2:

# import bisect

# def sort_me(courses):
    # temp = [(i.split('-')[1], i.split('-')[0]) for i in courses]
    # d = []
    # for i in temp:
        # bisect.insort(d, i)
    # result = [n[1] + '-' + str(n[0]) for n in d]
    # return result

# ---------------------------------------------------
print(sort_me(['aeb-1305', 'site-1305', 'play-1215', 'web-1304', 'site-1304', 'beb-1305']))

