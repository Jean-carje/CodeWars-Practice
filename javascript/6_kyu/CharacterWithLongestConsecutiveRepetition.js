// kata
// https://www.codewars.com/kata/586d6cefbcc21eed7a001155/

//--------------------------------------------------
// Solution:

function longestRepetition(s) {
  let ar = [];
  let w = s.charAt(0);
  let c = 0;
  let res = ["", 0];

  for (let i = 0; i <= s.length; i++) {
    if (w === s.charAt(i)) {
      c += 1;
    } else {
      ar.push([w, c]);
      w = s.charAt(i);
      c = 1;
    }
  }
  for (let el of ar) {
    if (res[1] < el[1]) {
      res = el;
    }
  }
  return res;
}


//--------------------------------------------------

console.log(longestRepetition("aaaabb"), ["a", 4]);
console.log(longestRepetition("bbbaaabaaaa"), ["a", 4]);
console.log(longestRepetition("cbdeuuu900"), ["u", 3]);
console.log(longestRepetition("abbbbb"), ["b", 5]);
console.log(longestRepetition("aabb"), ["a", 2]);
console.log(longestRepetition(""), ["", 0]);
console.log(longestRepetition("ba"), ["b", 1]);

