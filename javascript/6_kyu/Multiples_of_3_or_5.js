// Kata link:
// https://www.codewars.com/kata/514b92a657cdc65150000006/

// -------------------------------------
// Instructions:
/*
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

Note: If the number is a multiple of both 3 and 5, only count it once. Also, if a number is negative, return 0(for languages that do have them)

Courtesy of projecteuler.net
*/

// -------------------------------------
// Solution 1:

function solution(number) {
    let n = 0;
    for (let i = 1; i < number; i++) {
        if (i % 3 == 0 && i % 5 == 0) { n += i; } 
        else if (i % 3 == 0) { n += i; } 
        else if (i % 5 == 0) { n += i; }
    }
    return n;
}

// Solution 2:
// function solution(number) {
//     let n = 0;
//     for(var i = 3; i < number; i++){
//       if(i % 3 == 0 || i % 5 == 0){
//         n += i;
//       }
//     }
//     return n;
// }

// -------------------------------------

console.log(solution(10), " = (23)" )