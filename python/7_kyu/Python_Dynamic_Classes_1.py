# kata
# https://www.codewars.com/kata/55ddb0ea5a133623b6000043

# -----------------------------------------------
# Problem:
# Change name of class


# Note: Proposed function should allow only names with alphanumeric chars
# (upper & lower letters plus ciphers), but starting only with upper case
# letter. In other case it should raise an exception.
# Disclaimer: there are obviously betters way to check class name than in
# example cases, but let's stick with that, that Timmy yet has to learn them.

# -----------------------------------------------
# Solution:


def class_name_changer(cls, s):
    if not s.isalnum() or not s[0].isupper():
        raise Exception('Invalid')
    cls.__name__ = s


# -----------------------------------------------
# Test:

class MyClass:
    pass

myObject = MyClass()
print(MyClass.__name__)

class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__ == "UsefulClass")

class_name_changer(MyClass, "SecondUsefulClass")
print(MyClass.__name__ == "SecondUsefulClass")

