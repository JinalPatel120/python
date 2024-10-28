// create an object
let name = { name: "jinal", age: 67 };
console.log(name.name);
console.log(name.age);

const person = new Object();
person.firstname = "john";
person.lastname = "lathiya";
person.age = 22;

console.log(person);
console.log(person.firstname);
console.log(person.lastname);

const data = {
  firstname: "jinal",
  lastname: "lathiya",
};

console.log(data.firstname);
console.log(data["firstname"]);
console.log(data["lastname"]);

const data1 = {
  fname: "jinal",
  lname: "lathiya",
  age: function () {
    return this.fname + " " + this.lname;
  },
};
console.log(data1);
console.log(data1.age);

const personData = {
  firstname: "jinal",
  lastname: "lathiya",
  age: 20,
};
const x = personData;
console.log(personData, "person data");
console.log(x.age, "age");

personData.nationality = "English";
console.log(personData.nationality);
console.log(personData);

delete personData.age;
console.log(personData);
console.log(personData.age);

const myObj = {
  name: "jinal",
  age: 20,
  myCars: {
    car1: "toyoto",
    car2: "honda",
    car3: "fiat",
  },
};
console.log(myObj);
console.log(myObj.age);
console.log(myObj.myCars.car1);
console.log(myObj.myCars["car1"]);
console.log(myObj["myCars"]["car1"]);

// object
const personData1 = {
  fname: "hello",
  lname: "lathiya",
};
// object method
personData1.name = function () {
  return this.fname + " " + this.lname;
};
console.log(personData1.name());

personData1.name1 = function () {
  return (this.fname + " " + this.lname).toUpperCase();
};

console.log(personData1.name1());
const person2 = {
  firstname: "diya",
  lastname: "lathiya",
};
const person3 = {
  firstname: "jinal",
  lastname: "lathiya",
};
Object.assign(person3, person2); // Object.assign() copies properties froma source object to a target object.
let text = Object.entries(person3);
console.log(text);

// javascript object constructor

const person4 = {
  firstname: "poorvi",
  lastname: "kakadiya",
};

let text1 = person4.constructor;
console.log(text1);

const person5 = {
  firstname: "bhumi",
  lastname: "vithani",
};
const text3 = Object.create(person5);
text3.firstname = "dixit";
console.log(person5.firstname + " and " + text3.firstname);

// javascript object define properties
const person6 = {
  firstname: "hina",
  lastname: "lathiya",
};
Object.defineProperties(person6, {
  language: { value: "english" },
  year: { value: "hello" },
});

console.log(person6.language + " and " + person6.year);
console.log(person6);

const person7 = {
  fisrtname: "john",
  lastname: "doe",
  age: 50,
};
Object.freeze(person7);
let text4;
try {
  person7.age = 51;
  text4 = Object.values(person7);
} catch (err) {
  text4 = err;
}
console.log(text4); // Object.freeze methods prevent any changes to an object.

const fruits = [
  ["apples", 300],
  ["pears", 900],
  ["bananas", 500],
];

const MyObj = Object.fromEntries(fruits); // creates an object from list of key/value pair
console.log(MyObj);

// javascript arrays
//arrary -- it is special variable which can hold more than 1 value

const cars = ["toyato", "BMW", "Audi"];
console.log(cars);
console.log(cars[0]);
console.log(cars[2]);
console.log(cars.toString());
console.log(cars.length);
console.log(cars.sort());

const data2 = ["john", "Doe", 90];
console.log(data2);
console.log(data2.toString());
console.log(data2[2]);
console.log(data2.length - 1);

const data3 = {
  fname: "helo",
  laname: "lathiya",
  age: 90,
};

console.log(data3.age);
console.log(data2.length - 1);
console.log(data2);
console.log(data2.length);
console.log(data2.length - 1);
let sort1 = data2[data2.length - 2];
console.log(sort1);

let veg = ["onion", "tomato", "potato", "orange"];
let n = "";

// for loop
for (let i = 0; i < veg.length; i++) {
  n += veg[i];
}
console.log(n);

// for in loop -- statement loops through the properties of an object.

for (let i in veg) {
  n += veg[i];
}
console.log("for in loop", n);

// for of loop  -- loops through the values of an iterable object

for (let i of veg) {
  n += i;
}
console.log("for of loop", n);

// array.forEach() // callback is a function passed as an argument to another function.
const numbers1 = [45, 5, 9, 19, 20];
let txt = " ";

numbers1.forEach(myFunction);
function myFunction(value) {
  txt += value;
}

console.log(txt);

const cars1 = [];
cars1[0] = "volvo";
cars1[1] = "Audi";
cars1[2] = "BMW";
console.log(cars1);
cars1[0] = "venue";
console.log(cars1);
let cars3 = cars1[cars1.length - 2];
console.log(cars3);
cars1.push("jinal");
console.log(cars1);
cars1[7] = "hello";
console.log(cars1);

// difference between arrays and objects
// arrays are numbered indexes and objects are named indexes.
const points = new Array(40, 100, 1, 5, 25, 20);
const points1 = [40, 100, 1, 5, 25, 20];
console.log(points);
console.log(points1);

const fruits1 = ["banana", "orange", "apple"];
let type = typeof fruits;
console.log(type);

// nested arrays and objects

const myAbc = {
  name: "john",
  age: 30,
  cars: [
    { name: "ford", models: ["fiesta", "focus"] },
    { name: "bmw", models: ["320", "X3"] },
  ],
};

console.log(myAbc);
console.log(myAbc.cars);
let k = "";
for (let i in myAbc.cars) {
  k += myAbc.cars[i].name;
  for (let j in myAbc.cars[i].models) {
    k += myAbc.cars[i].models[j];
  }
}
console.log(k);

const veg1 = ["banana", "orange", "apple", "mango"];
let vege = veg1.at(1);
console.log(vege);

veg1.pop();
console.log(veg1);

let position = veg1.indexOf("orange");
console.log(position);
let pos = veg1.lastIndexOf("orange");
console.log(pos);
let v = veg1.includes("apple");
console.log(v);

const num1 = [3, 4, 5, 6, 7, 8, 9];
let first = num1.find(myXyz);
function myXyz(value, index, array) {
  return value < 5;
}
console.log(first);

const temp = [27, 28, 90, 54, 32, 43, 54];
let high = temp.findLast((x) => x > 40);
console.log(high);

// this is my callback function

function myDisplay(helo) {
  return helo;
}

function myCalculator(num1, num2) {
  let sum = num1 + num2;
  myDisplay(sum);
}

console.log(myCalculator(5, 5));

// asynchronous function -- functions running in parallel with other functions are called asynchronous

// js promise objects
// promise code that links producing code and consuming code

class ClassName {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
}

const car1 = new ClassName("ford", 2012);
const car2 = new ClassName("toyoto", 2025);

console.log(car1.name);
console.log(car2.year);

class Car {
  constructor(name, year) {
    this.name = name;
    this.year = year;
  }
  age() {
    const date = new Date();
    return date.getFullYear() - this.year;
  }
}

const myCar = new Car("ford", 2023);
console.log(myCar);
console.log(myCar.age());

// objects getter and setter methods

const person1 = {
  name: "jianl",
  age: 22,
  get age1() {
    return this.age;
  },
};

console.log(person1.age1);

const personData2 = {
  name: "jinal",
  age: 21,
  get age1() {
    return this.age;
  },
  set age2(age) {
    this.age = age;
  },
};

console.log(personData2.age1);
console.log(personData2);
personData2.age2 = 22;
console.log(personData2.age);

const fruit = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruit.reverse());
console.log(fruit.sort());
console.log(fruit.toSorted());
console.log(fruit.toReversed());

//object constructor

function Person(first, last, age, eye) {
  this.firstname = first;
  this.lastname = last;
  this.age = age;
  this.eye = eye;
}

const p = new Person("jinal", "lathiya", 22, "blue");
console.log(p.firstname);
console.log(p.lastname);
console.log(p.age);
console.log(p.eye);

let e = 10;
let f = 20;
let g = "20";
let result = e + f + g;
console.log(result);
// e="10";
// f="20";
// g="10";
// result=e+f+g
// console.log(result)

let ab = "10";
let bc = "20";
let cd = "10";
let res = ab + cd + bc;
console.log(res);
let type1 = typeof e;
console.log(type1);

const n2 = [23, 32, 43, 5, 46, 65, 76, 90];
let txt1 = "";
n2.forEach(myFunction1);

function myFunction1(value) {
  txt1 += value;
}

console.log(txt1);

const fru = new Map([
  ["apple", 500],
  ["banana", 300],
  ["orange", 30],
]);

let np = fru.get("banana");
console.log(np);

//javascript Errors handling

// const adddert='';
// try{
//     adddert("welcome guest");
// }
// catch(err){
//     console.log(err.message);
// }

// try{
//     nonExistFunction();
// }
// catch(error){
//     console.error(error);
// }

myFunc();

function myFunc() {
  "use strict";

  let y = 4.5;
}

const fr = ["apples", "bananas", "oranges"];
console.log(Array.isArray(fr));

//javascript type conversion
