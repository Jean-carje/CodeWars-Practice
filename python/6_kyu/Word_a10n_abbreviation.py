# kata:
# https://www.codewars.com/kata/5375f921003bf62192000746/

# --------------------------------------------------
# Solution:

def abbreviate(s):
    if len(s) > 3:
        temp = []
        word = ''
        result = ''
        for ch in s:
            if ch.isalpha():
                word += ch
            else:
                temp.append(word)
                temp.append(ch)
                word = ''
        temp.append(word if word else '')
        for i in temp:
            if len(i) > 3:
                result += i[0] + str(len(i) - 2) + i[-1]
            else:
                result += i
        return result
    return s


# --------------------------------------------------

print(abbreviate("internationalization"), "i18n")
print(abbreviate("accessibility"), "a11y")
print(abbreviate("Accessibility"), "A11y")
print(abbreviate("elephant-ride"), "e6t-r2e")

