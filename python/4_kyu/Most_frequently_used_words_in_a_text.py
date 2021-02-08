# Kata link:
# https://www.codewars.com/kata/51e056fe544cf36c410000fb/

# -------------------------------------
# Solution:
import re
from collections import Counter

def top_3_words(text):
    words = re.findall("[a-z']+", text.lower())
    return [el[0] for el in Counter(words).most_common(3) if re.search('[a-z]', el[0])]

