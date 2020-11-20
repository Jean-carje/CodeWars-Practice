# Kata link:
# https://www.codewars.com/kata/5a793fdbfd8c06d07f0000d5/train/python

# -------------------------------------
# -------------------------------------
# Solution:
def solve(st):
    tp = ''
    st = st.replace('(', '').replace(')', '')
    for i in range(len(st)- 1,-1,-1):
        if st[i].isalpha():
            tp += st[i]
        
        if st[i].isdigit():
            tp = tp * int(st[i])
    return tp[::-1]

# ---------------------------------- 

print(solve("3(ab)"),"ababab")
print(solve("2(a3(b))"),"abbbabbb")
print(solve("3(b(2(c)))"),"bccbccbcc")
