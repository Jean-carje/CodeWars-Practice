// Kata link:
// https://www.codewars.com/kata/523f5d21c841566fde000009/

// -------------------------------------
// Instructions:
/*
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b.

    arrayDiff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

    arrayDiff([1,2,2,2,3],[2]) == [1,3]
*/
// -------------------------------------
// Solution:

function arrayDiff(a, b) {
    if (a.length > 0 && b.length > 0) {
        return a.filter(x => !b.includes(x));
    }
    return a;
}
// -------------------------------------
// Basic Tests
console.log(arrayDiff([], [4,5]), [], "a was [], b was [4,5]");
console.log(arrayDiff([3,4], [3]), [4], "a was [3,4], b was [3]");
console.log(arrayDiff([1,8,2], []), [1,8,2], "a was [1,8,2], b was []");
console.log(arrayDiff([1,2,2,2,3],[2]));