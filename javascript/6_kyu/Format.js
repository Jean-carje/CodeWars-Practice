// Kata link:
// https://www.codewars.com/kata/53368a47e38700bd8300030d

// -------------------------------------
// Instructions:
/*
list([ {name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'} ])
// returns 'Bart, Lisa & Maggie'

list([ {name: 'Bart'}, {name: 'Lisa'} ])
// returns 'Bart & Lisa'

list([ {name: 'Bart'} ])
// returns 'Bart'

list([])
// returns ''
*/

// -------------------------------------
// Solution:

function list(names) {
  let ar = names.map((x) => {return x.name;});
  let s = ar.slice(0, -1).join(", ");
  return names.length > 1 ? s + " & " + ar.slice(-1) : ar.join("");
}

// -------------------------------------
// Basic Tests
console.log(list([{name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'}, {name: 'Homer'}, {name: 'Marge'}]) == 'Bart, Lisa, Maggie, Homer & Marge')
console.log(list([{name: 'Bart'}, {name: 'Lisa'}, {name: 'Maggie'}]) == 'Bart, Lisa & Maggie')
console.log(list([{name: 'Bart'}, {name: 'Lisa'}]) == 'Bart & Lisa')
console.log(list([{name: 'Bart'}]) == 'Bart')
console.log(list([]) == '')
