// Kata link:
// https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

// -------------------------------------
// Solution:

function persistence(num) {
  let count = 0;
  num = String(num).split("");

  while (num.length > 1) {
    count += 1;

    let n = 1;
    for (let i of num) {
      n *= Number(i);
    }
    num = String(n);
  }
  return count;
}


// -------------------------------------
// Basic Tests
console.log(persistence(39), 3);
console.log(persistence(4), 0);
console.log(persistence(25), 2);
console.log(persistence(999), 4);
