// Kata link:
// https://www.codewars.com/kata/56f7f8215d7c12c0e7000b19/

// -------------------------------------
// Solution 1:

class Person {
  constructor(firstName = "John", lastName = "Doe", age = 0, gender = "Male") {
    this.firstName = firstName;
    this.lastName = lastName;
    this.age = age;
    this.gender = gender;
  }

  sayFullName() {
    return `${this.firstName} ${this.lastName}`;
  }

  static greetExtraTerrestrials(raceName) {
    return `Welcome to Planet Earth ${raceName}`;
  }
}


// -------------------------------------
// Basic Tests

console.log(new Person().firstName == "John");
console.log(new Person().lastName == "Doe");
console.log(new Person().age == 0);
console.log(new Person().gender == "Male");
console.log(new Person().sayFullName() == "John Doe");

