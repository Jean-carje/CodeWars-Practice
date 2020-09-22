// Kata link:
// https://www.codewars.com/kata/59dd2c38f703c4ae5e000014/train/javascript

// -------------------------------------
// Instructions:
/*
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

isIsogram("Dermatoglyphics") == true
isIsogram("aba") == false
isIsogram("moOse") == false // -- ignore letter case
*/
// -------------------------------------
// Solution:

function isIsogram(str){
    if (str.length == 0) { return true; } 
    else {
        let ar = str.toLowerCase().split("");
        let arr = Array.from(ar); 
        const repeat = (item) => arr.slice(ar.indexOf(item)+1).includes(item);
        return ar.every(repeat);
    }
}


// -------------------------------------
// Basic Tests
console.log( isIsogram("Dermatoglyphics"), true );
console.log( isIsogram("isogram"), true );
console.log( isIsogram("aba"), false, "same chars may not be adjacent" );
console.log( isIsogram("moOse"), false, "same chars may not be same case" );
console.log( isIsogram("isIsogram"), false );
console.log( isIsogram(""), true, "an empty string is a valid isogram" );