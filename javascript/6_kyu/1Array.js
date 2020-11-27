// kata
// https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9/

//--------------------------------------------------
// Solution:

function upArray(arr) {
  if (arr.length > 1 && arr.every(n => n >= 0 && 10 > n && Number.isInteger(n))) {
    if (arr.length > 15) {
      let last = arr.slice(arr.lastIndexOf(2), arr.length);
      let tp = Number(last.join('')) + 1;
      return Array.from(arr.slice(0, arr.lastIndexOf(2)).concat(Array.from(String(tp), i => Number(i))));
    }
    let temp = Number(arr.join('')) + 1;
    return Array.from(String(temp), i => Number(i));
  }
  return null;
}

//--------------------------------------------------
//console.log(upArray([2, 3, 9]), [2, 4, 0]);
//console.log(upArray([4, 3, 2, 5]), [4, 3, 2, 6]);
//console.log(upArray([1, -9]), null);


