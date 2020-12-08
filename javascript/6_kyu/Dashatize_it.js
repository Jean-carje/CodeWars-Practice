// kata
// https://www.codewars.com/kata/58223370aef9fc03fd000071/train/javascript

//--------------------------------------------------
// Solution:

function dashatize(num) {
  let res = 'NaN';
  if (!Number.isNaN(num)) {
    let str = String(Math.abs(num));
    res = str[0]
    for (let i = 1; i < str.length; i++) {
      if (Number(str[i]) % 2 == 0) {
        if (res[-1] != '-' && Number(res[res.length - 1]) % 2 != 0) {
          res += '-' + str[i];
          continue;
        }
        res += str[i];
      } else {
        res += '-' + str[i];
      }
    }
  }
  return res;
}


//--------------------------------------------------

console.log(dashatize(274), "2-7-4", "Should return 2-7-4");
console.log(dashatize(5311), "5-3-1-1", "Should return 5-3-1-1");
console.log(dashatize(86320), "86-3-20", "Should return 86-3-20");
console.log(dashatize(974302), "9-7-4-3-02", "Should return 9-7-4-3-02");



