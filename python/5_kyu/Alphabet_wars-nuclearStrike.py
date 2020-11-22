# Kata:
# https://www.codewars.com/kata/59437bd7d8c9438fb5000004/

# ---------------------------------------------------
# Solution:

import re


def alphabet_war(alph):
    if not alph.count('#'):
        return re.sub(r"[\[\]]", "", alph)

    result = ''
    rgx = re.compile(r'([a-z#]*)\[([a-z]+)\](?=([a-z#]*))')

    for r in rgx.findall(alph):
        if (r[0] + r[2]).count('#') < 2:
            result += ''.join(r[1])
        else:
            result += ''
    return result


# ---------------------------------------------------
# Test:

print(alphabet_war('[a]#[b]#[c]'), 'ac')
print(alphabet_war('[a]#b#[c][d]'), 'd')
print(alphabet_war('[a][b][c]'), 'abc')
print(alphabet_war('##a[a]b[c]#'), 'c')
print(alphabet_war('abde[fgh]ijk'), 'abdefghijk')
print(alphabet_war('ab#de[fgh]ijk'), 'fgh')
print(alphabet_war('ab#de[fgh]ij#k'), '')
print(alphabet_war('##abde[fgh]ijk'), '')
print(alphabet_war('##abde[fgh]'), '')
print(alphabet_war('##abcde[fgh]'), '')
print(alphabet_war('abcde[fgh]'), 'abcdefgh')
print(alphabet_war('##abde[fgh]ijk[mn]op'), 'mn')
print(alphabet_war('#abde[fgh]i#jk[mn]op'), 'mn')
print(alphabet_war('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#'), 'abijk')
