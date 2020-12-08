# kata:
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/

# --------------------------------------------------
# Solution:
import string

def is_pangram(s):
    for l in string.ascii_lowercase:
        if l not in s.lower():
            return False
    return True


# --------------------------------------------------


pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram), True)


