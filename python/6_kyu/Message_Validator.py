# kata:
# https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc/

# --------------------------------------------------
# Solution:
import re


def is_a_valid_message(message):
    if len(message) > 1 and (not message[0].isdigit() or message[-1].isdigit()):
        return False
    numbs = re.findall(r"\d+", message)
    words = [t for t in re.split(r"\d+", message) if t != '']
    for n, w in zip(numbs, words):
        if int(n) != len(w):
            return False
    return True

# --------------------------------------------------

