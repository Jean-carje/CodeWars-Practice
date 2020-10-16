// Kata link:
// https://www.codewars.com/kata/563cf89eb4747c5fb100001b

// -------------------------------------
// Instructions:
/*

Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.

Examples
  removeSmallest([1,2,3,4,5]) = [2,3,4,5]
  removeSmallest([5,3,2,1,4]) = [5,3,2,4]
  removeSmallest([2,2,1,2,1]) = [2,2,2,1]
*/

// -------------------------------------
// Solution 1:

function removeSmallest(numbers) {
  if (!numbers) {
    return [];
  }
  let min = Math.min(...numbers);
  let ind = numbers.indexOf(min);
  return numbers.slice(0, ind).concat(numbers.slice(ind + 1));
}


// -------------------------------------
// Basic Tests

console.log(removeSmallest([1, 2, 3, 4, 5]), [2, 3, 4, 5]);
console.log(removeSmallest([5, 3, 2, 1, 4]), [5, 3, 2, 4]);
console.log(removeSmallest([2, 2, 1, 2, 1]), [2, 2, 2, 1]);
console.log(removeSmallest([]), [])

