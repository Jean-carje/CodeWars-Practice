// kata
// https://www.codewars.com/kata/586d6cefbcc21eed7a001155/

//--------------------------------------------------
// Solution:

function longestRepetition(s) {
  let res = ['', 0];
  let w = '';
  let c = 0;
  for (let i = 0; i < s.length; i++) {
    w = s.charAt(i)
    c += 1
    if (res[-2] != s.charAt(i - 1) && res[-1] < c) {
      res.push(w);
      res.push(c)
      c = 0
    }
  }
  return res
}


//--------------------------------------------------

console.log(longestRepetition("aaaabb"), ["a", 4]);
console.log(longestRepetition("bbbaaabaaaa"), ["a", 4]);
//console.log(longestRepetition("cbdeuuu900"), ["u", 3]);
//console.log(longestRepetition("abbbbb"), ["b", 5]);
//console.log(longestRepetition("aabb"), ["a", 2]);
//console.log(longestRepetition(""), ["", 0]);
//console.log(longestRepetition("ba"), ["b", 1]);

