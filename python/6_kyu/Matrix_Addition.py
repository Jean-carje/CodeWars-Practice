# Kata link:
# https://www.codewars.com/kata/526233aefd4764272800036f/

# -------------------------------------
# Instructions:
'''
Write a function that accepts two square matrices (N x N two dimensional
arrays), and return the sum of the two. Both matrices being passed into
the function will be of size N x N (square), containing only integers.

How to sum two matrices:

Take each cell [n][m] from the first matrix, and add it with the same 
[n][m] cell from the second matrix. This will be cell [n][m] of the 
solution matrix.

Visualization:

    |1 2 3|     |2 2 1|     |1+2 2+2 3+1|     |3 4 4|
    |3 2 1|  +  |3 2 3|  =  |3+3 2+2 1+3|  =  |6 4 4|
    |1 1 1|     |1 1 3|     |1+1 1+1 1+3|     |2 2 4|
Example
    matrixAddition(
    [ [1, 2, 3],
        [3, 2, 1],
        [1, 1, 1] ],
    //      +
    [ [2, 2, 1],
        [3, 2, 3],
        [1, 1, 3] ] )

    // returns:
    [ [3, 4, 4],
        [6, 4, 4],
        [2, 2, 4] ]
'''
# -------------------------------------
# Soluction 

def matrix_addition(a, b):
    return [[x + y for x, y in zip(first, second)] for first, second in zip(a,b)]


# -------------------------------------
print('Basic Tests:')
print(matrix_addition(
  [ [1, 2],
    [1, 2] ],
#     +
  [ [2, 3],
    [2, 3] ] )
    ==
  [ [3, 5],
    [3, 5] ] )

print(matrix_addition(
  [ [1] ],
#    +
  [ [2] ] )
   ==
  [ [3] ] )

print(matrix_addition(
  [ [1, 2, 3],
    [3, 2, 1],
    [1, 1, 1] ],
#       +
  [ [2, 2, 1],
    [3, 2, 3],
    [1, 1, 3] ] )
    ==
  [ [3, 4, 4],
    [6, 4, 4],
    [2, 2, 4] ] )