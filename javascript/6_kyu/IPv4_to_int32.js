// Kata link:
// https://www.codewars.com/kata/52ea928a1ef5cfec800003ee/

// -------------------------------------
// Solution:

function ipToInt32(ip) {
    return ip.split('.').reduce((a, b) => {return a * 256 + +b})
}


// -------------------------------------
// Basic Tests
console.log(ipToInt32("128.32.10.1"))
