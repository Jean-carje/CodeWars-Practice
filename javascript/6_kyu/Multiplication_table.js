// kata
// https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08/

//--------------------------------------------------
// Solution:

let multiplicationTable = function (size) {
  let result = [[...Array(size + 1).keys()]];
  result[0].shift();
  for (let n = 0; n < size - 1; n++) {
    let tp = [];
    for (let i = 0; i < size; i++) {
      tp.push(result[n][i] + result[0][i]);
    }
    result.push(tp);
  }
  return result;
}

//--------------------------------------------------
console.log(multiplicationTable(3), [[1, 2, 3], [2, 4, 6], [3, 6, 9]]);
