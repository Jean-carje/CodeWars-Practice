// Kata link:
// https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/

// ---------------------------------------
// ---------------------------------------
// Solution:

function duplicateEncode(word) {
    let result = '';
    word = word.toLowerCase();
    for (let i = 0; i < word.length; i++) {
        if (word.indexOf(word[i]) == i && i == word.lastIndexOf(word[i])) {
            result += '(';
        } else {
            result += ')';
        }
    }
    return result;
}


// -------------------------------------
// Basic Tests
console.log(duplicateEncode("din"), "(((");
console.log(duplicateEncode("recede"), "()()()");
console.log(duplicateEncode("Success"), ")())())", "should ignore case");
console.log(duplicateEncode("(( @"), "))((");
