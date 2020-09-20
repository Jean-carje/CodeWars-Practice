# Kata link:
# https://www.codewars.com/kata/520446778469526ec0000001/

# -------------------------------------
# Instructions:
'''
Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:

    # should return True
    same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

    # should return False 
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
    same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
'''

# -------------------------------------
# Solution:

def same_structure_as(original,other):
    cont = True
    if len(original) != len(other) or type(original) != type(other):
        return False
    for x, y in zip(original, other):
        if type(x) != type(y):
            return False
        if type(x) == list and type(y) == list:
            return same_structure_as(x,y)
    return True

# -------------------------------------
# Basic Tests:

print(same_structure_as([1,[1,1]],[2,[2,2]]) == True and "[1,[1,1]] same as [2,[2,2]]")
print(same_structure_as([1,[1,1]],[[2,2],2]) == False and "[1,[1,1]] not same as [[2,2],2]")

print(" should return True:")
print(same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ]) )
print(same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] ))
print(same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] ))

print(" should return False:")
print(same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] ))
print(same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )) 
