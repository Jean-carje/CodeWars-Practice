// kata
// https://www.codewars.com/kata/556e0fccc392c527f20000c5/train/javascript

//--------------------------------------------------
// Solution:

function Xbonacci(signature, n) {
  let x = signature.length;
  let result = [...signature];
  if (x > 1) {
    for (let i = 0; i < n - x; i++) {
      result.push(result.slice(-x).reduce((a, b) => a + b));
    }
  }
  else if (x == 1 && n > 1) {
    return Array(n).fill(result[0]);
  }
  return result.slice(0, n);
}

//--------------------------------------------------

console.log(Xbonacci([0, 1], 10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]);
console.log(Xbonacci([1, 1], 10), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]);
console.log(Xbonacci([0, 0, 0, 0, 1], 10), [0, 0, 0, 0, 1, 1, 2, 4, 8, 16]);
console.log(Xbonacci([1, 0, 0, 0, 0, 0, 1], 10), [1, 0, 0, 0, 0, 0, 1, 2, 3, 6]);
console.log(Xbonacci([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256]);



