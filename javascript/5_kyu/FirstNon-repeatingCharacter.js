// kata
// https://www.codewars.com/kata/52bc74d4ac05d0945d00054e/train/javascript

//--------------------------------------------------
// Solution:

function firstNonRepeatingLetter(s) {
  for (let i of new Set(s)) {
    if (s.toLowerCase().indexOf(i.toLowerCase()) === s.toLowerCase().lastIndexOf(i.toLowerCase())) {
      return i;
    }
  }
  return "";
}


//--------------------------------------------------




