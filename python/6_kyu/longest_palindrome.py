# Kata link:
# https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python

# -------------------------------------
# Instructions:
'''
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
'''
# -------------------------------------
# Solution
def longest_palindrome (s):
    if len(s) == 0:
        return 0
    else:
        length = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    if len(sub) > length:
                        length = len(sub)
        return length

# -------------------------------------
# Basic Tests
print(longest_palindrome("a"),"=", 1)
print(longest_palindrome("aa"),"=", 2)
print(longest_palindrome("baa"),"=", 2)
print(longest_palindrome("aab"),"=", 2)
print(longest_palindrome("abcdefghba"),"=", 1)
print(longest_palindrome("baablkj12345432133d"),"=", 9)
