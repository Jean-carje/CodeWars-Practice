// kata:
// https://www.codewars.com/kata/554ca54ffa7d91b236000023

// ----------------------------------------------
// solution:

function deleteNth(arr, n) {
  let rep = {};
  arr.forEach((x) => {rep[x] = (rep[x] || 0) + 1;});
  for (let i in rep) {
    if (rep[i] > n) {
      for (let _ = 0; _ < rep[i] - n; _++) {
        arr.splice(arr.lastIndexOf(+i), 1);
      }
    }
  }
  return arr;
}

// ----------------------------------------------
// solution:

console.log(deleteNth([20, 37, 20, 21], 1))
console.log(deleteNth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))
