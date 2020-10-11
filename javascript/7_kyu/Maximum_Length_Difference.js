// Kata link:
// https://www.codewars.com/kata/5663f5305102699bad000056

// // -------------------------------------
// Instructions:
/*
 *
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z.
Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
	a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
	a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
	mxdiflg(a1, a2) --> 13

*/
// -------------------------------------
// Solution 1:

function mxdiflg(a1, a2) {
	let result = Math.max(...a1.map(x => {
		return Math.max.apply(null, a2.map(y => {
			return Math.abs(x.length - y.length);
		}));
	}));
	return result > 0 ? result : -1;
}


// -------------------------------------
// Basic Tests

var s1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"];
var s2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"];
console.log(mxdiflg(s1, s2) === 13);

var s1 = [];
var s2 = [];
console.log(mxdiflg(s1, s2) === -1);
