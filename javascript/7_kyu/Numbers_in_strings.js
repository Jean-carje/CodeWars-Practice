// Kata link:
// https://www.codewars.com/kata/59dd2c38f703c4ae5e000014/train/javascript

// -------------------------------------
// Instructions:
/*
In this Kata, you will be given a string that has lowercase letters and numbers. Your task is to compare the number groupings and return the largest number.

For example, solve("gh12cdy695m1") = 695, because this is the largest of all number groupings.

*/
// -------------------------------------
// Solution:

function solve(s){
    let temp = 0;
    for (let i of s.match(/(\d+)/g)) {
        if (Number(i) > temp) {
            temp = Number(i);
        }
    }
    return temp;
};

// -------------------------------------
// Basic Tests
console.log(solve('gh12cdy695m1'),695);
console.log(solve('2ti9iei7qhr5'),9);
console.log(solve('vih61w8oohj5'),61);
console.log(solve('f7g42g16hcu5'),42);
console.log(solve('lu1j8qbbb85'),85);