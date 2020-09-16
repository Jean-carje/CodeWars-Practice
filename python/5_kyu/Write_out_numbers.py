# Kata link:
# https://www.codewars.com/kata/52724507b149fa120600031d/

# -------------------------------------
# Instructions:
'''
Create a function that transforms any positive number to a string representing the number in words. The function should work for all numbers between 0 and 999999.

number2words(0)  ==>  "zero"
number2words(1)  ==>  "one"
number2words(9)  ==>  "nine"
number2words(10)  ==>  "ten"
...
'''
# -------------------------------------
# Solution:

def number2words(n):
    specials = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    numb = str(n)
    temp = specials[10:-1][int(numb[0])].replace("teen", "ty")

    if n <= 20:
        return specials[n]
    elif 21 <= n < 100:
        if numb[-1] != "0":
            if n < 30: 
                return "twenty-" + number2words(int(numb[-1]))
            elif n < 50: 
                return "forty-" + number2words(int(numb[-1]))
            else:
                return temp + '-' + number2words(int(numb[-1]))
        else:
            if n == 20: 
                return "twenty"
            elif n == 40: 
                return "forty"
            else:
                return temp
    elif 100 <= n < 1000:
        if numb[1:] == "00":
            return specials[int(numb[0])] + ' hundred'
        else:
            return specials[int(numb[0])] + ' hundred ' + number2words(int(numb[1:]))
    elif 1000 <= n < 10000:
        if numb[1:] == "000":
            return specials[int(numb[0])] + ' thousand'
        else:
            return specials[int(numb[0])] + ' thousand ' + number2words(int(numb[1:]))
    elif 10000 <= n < 100000:
        if numb[1:] == "0000":
            return number2words(int(numb[:2])) + ' thousand'
        else:
            return number2words(int(numb[:2])) + ' thousand ' + number2words(int(numb[2:]))
    else:
        if numb[1:] == "00000":
            return number2words(int(numb[:3])) + ' hundred'
        else:
            return number2words(int(numb[:3])) + ' thousand ' + number2words(int(numb[3:]))


# -------------------------------------
# Basic Tests
print(number2words(0), "\n\t # zero")
print(number2words(1), "\n\t # one")
print(number2words(8), "\n\t # eight")
print(number2words(10), "\n\t # ten")
print(number2words(19), "\n\t # nineteen")
print(number2words(20), "\n\t # twenty")
print(number2words(22), "\n\t # twenty-two")
print(number2words(54), "\n\t # fifty-four")
print(number2words(80), "\n\t # eighty")
print(number2words(98), "\n\t # ninety-eight")
print(number2words(100), "\n\t # one hundred")
print(number2words(301), "\n\t # three hundred one")
print(number2words(793), "\n\t # seven hundred ninety-three")
print(number2words(800), "\n\t # eight hundred")
print(number2words(650), "\n\t # six hundred fifty")
print(number2words(1000), "\n\t # one thousand")
print(number2words(1003), "\n\t # one thousand three")
print(number2words(90000), "\n\t # ninety-nine thousand nine hundred ninety-nine")
print(number2words(202448), "\n\t # two hundred two thousand four hundred forty-eight")
print(number2words(888888), "\n\t # eight hundred eighty-eight thousand eight hundred eighty-eight")