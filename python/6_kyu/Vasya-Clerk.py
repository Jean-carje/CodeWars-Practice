# kata:
# https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8/

# --------------------------------------------------
# Solution:
def tickets(people):
    a25 = 0
    a50 = 0
    a100 = 0
    for p in people:
        if p == 100:
            if a25 >= 1 and a50 >= 1:
                a25 -= 1
                a50 -= 1
                a100 += 1
            elif a25 >= 3:
                a25 -= 3
                a50 -= 1
            else:
                return "NO"
        elif p == 50:
            if a25 >= 1:
                a25 -= 1
                a50 += 1
            else:
                return "NO"
        else:
            a25 += 1
    return "YES"



# --------------------------------------------------



