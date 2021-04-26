# kata:
# https://www.codewars.com/kata/56a5d994ac971f1ac500003e/train/python

# --------------------------------------------------
def longest_consec(strarr, k):
    string = ""
    length = len(string)
    if k > 0:
        for i in range(len(strarr) - k + 1):
            temp = "".join(strarr[i:i + k])
            if len(temp) > length:
                string = temp
                length = len(string)
    return string

# --------------------------------------------------
print(longest_consec(["zone", "abigail", "theta", "form", "libe", "zas"], 2), "abigailtheta")

