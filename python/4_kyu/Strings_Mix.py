# Kata link:
# https://www.codewars.com/kata/5629db57620258aa9d000014/train/python

# -------------------------------------
# Solution:
from collections import Counter
from string import ascii_lowercase


def mix(s1, s2):
    s1_count = Counter(s1)
    s2_count = Counter(s2)
    temp = {}
    for l in ascii_lowercase:
        count1 = s1_count[l]
        count2 = s2_count[l]
        high = max(count1, count2)
        if max(count1, count2) > 1:
            if count1 > count2:
                tp = '1'
            elif count2 > count1:
                tp = '2'
            else:
                tp = '='
            temp[l] = (-high, tp + ":" + l * high)

    result = ''
    for el in sorted(temp, key=lambda x: temp[x]):
        result += ''.join(temp[el][1])
        result += '/'
    return result[:-1]


# -------------------------------------
# Basic Tests

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"
print(mix(s1, s2))
print(mix(s1, s2) == "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")

s1 = "mmmmm m nnnnn y&friend&Paul has heavy hats! &"
s2 = "my frie n d Joh n has ma n y ma n y frie n ds n&"
print(mix(s1, s2))
print(mix(s1, s2) == "1:mmmmmm/=:nnnnnn/1:aaaa/1:hhh/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss")

s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"
print(mix(s1, s2))
print(mix(s1, s2) == "=:aaaaaa/2:eeeee/=:fffff/1:tt/2:rr/=:hh")

