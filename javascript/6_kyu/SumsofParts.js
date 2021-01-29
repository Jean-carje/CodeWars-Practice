// kata
// https://www.codewars.com/kata/5ce399e0047a45001c853c2b/

//--------------------------------------------------
// Solution:

function partsSums(ls) {
  let res = []
  if (ls.length) {
    let ttl = ls.reduce((a, b) => a + b);
    res.push(ttl);
    for (let el of ls) {
      res.push(ttl -= el);
    }
  }
  return res.length ? res : [0];
}


//--------------------------------------------------

console.log(partsSums([0, 1, 3, 6, 10]));


