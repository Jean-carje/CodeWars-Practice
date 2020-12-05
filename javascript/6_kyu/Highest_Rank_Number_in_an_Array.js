// kata
// https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/javascript

//--------------------------------------------------
// Solution:


function highestRank(arr) {
  let n = 0, c = 0;
  for (let i of new Set(arr)) {
    let temp = arr.filter(j => j === i).length;
    if (temp > c) {
      n = i;
      c = temp;
    } else if (temp === c) {
      n = i > n ? i : n;
    }
  }
  return n;
}



//--------------------------------------------------

let arr = [12, 10, 8, 12, 7, 6, 4, 10, 12];
console.log(highestRank(arr), 12);



