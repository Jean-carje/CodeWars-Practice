// kata
// https://www.codewars.com/kata/520b9d2ad5c005041100000f/

//--------------------------------------------------
// Solution:

function pigIt(str) {
  let res = [];
  let arr = str.split(" ");
  for (let w = 0; w < arr.length; w++) {
    if (arr[w].charAt(arr[w].length - 1).match(/[a-z]|[A-Z]/i)) {
      res.push(arr[w].substr(1,) + arr[w].charAt(0) + 'ay')
    } else {
      res.push(arr[w]);
    }
  }
  return res.join(' ')
}


//--------------------------------------------------

console.log(pigIt('Pig latin is cool'), 'igPay atinlay siay oolcay')
console.log(pigIt('This is my string'), 'hisTay siay ymay tringsay')



