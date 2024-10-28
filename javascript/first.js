console.log("hello");

const student = {
  name: "jinal",
  cgpa: 88.4,
  city: "bhavnagar",
};

console.log(student.cgpa);

const product = {
  name: "pen",
  rating: 4,
  deal: true,
  price: 250,
};

console.log(product);

// Arithmetic operator

let a = 5;
let b = 2;

console.log("a+b=", a + b);

// conditional statements

let mode = "black";
let color;

if (mode == "black") {
  color = "dark";
}

if (mode == "white") {
  color = "light";
}

console.log("value of colour", color);

if (mode == "black") {
  color = "dark";
} else {
  color = "light";
}

console.log("color is", color);

let n = 12;

if (n % 2 == 0) {
  console.log("even");
} else {
  console.log("odd");
}

let age = 25;

let result = age >= 18 ? "adult" : "not adult";
console.log(result);


// let r=prompt("enter number to check that is multiple by 5 or not ? ")

// if (r%5==0){
//     console.log("yes multiple ")
//     localStorage.setItem("name", r);
// }
// else{console.log("not multiple")}

// let score=prompt('enter your score')
// let grade;

// if (score >80){
//     grade="A"
// }
// else if(score<80 & score >70){
//     grade="B"
// }
// else if (score<70 & score>=60){
//     grade="C"
// }
// else if(score<60 & score>=50){
//     grade="D"
// }
// else{
//     grade="E"
// }

// console.log("your score is",grade)

for (let i = 1; i <= 5; i++) {
  console.log("hello form jinal");
}

let sum = 0;

for (let i = 1; i <= 5; i++) {
  sum = sum + i;
}

console.log("sum is", sum);

let i = 1;

while (i <= 5) {
  console.log("i =", i);
  i++;
}

for (i = 1; i <= 101; i++) {
  if (i % 2 == 0) {
    console.log("even numbers are", i);
  }
}

// let guess=12
// let num=prompt("enter the number")

// while(num!==guess){
//     console.log('you entered wrong')
// }

// console.log('you guess the right number')

function myfunction(a, b) {
  c = a + b;
  console.log("result is", c);
}

myfunction(5, 3);

let arr = [21, 32, 54, 65, 87, 9, 87, 65, 54, 65];
console.log("array --", arr);
console.log(arr[4]);

for (i = 0; i < arr.length; i++) {
  console.log("helooo", arr[i]);
}

for (let i of arr) {
  console.log("for of", i);
}

// find average marks from list of array

let k = [54, 65, 87, 98, 76, 65, 43, 21, 43, 65, 87, 9];
let m = 0;

for (let i of k) {
  m += i;
}

console.log("average values", m / k.length);
console.log("m here", m);

/*for a given array with prices of 5 items ->

250,645,300,900,50, all items have an offer of 10% off on them. change the array to store final price after
applying offer.*/

let price = [250, 645, 300, 900, 50];

let dis = 0;
let j;

for (let i of price) {
  let val = i - 10;
  console.log("value after discount is", val);
}

function valid(x, y) {
  z = x + y;
  return z;
}

console.log(valid(5, 7));

let count = 0;

function CountVowels(msg) {
  for (let i of msg) {
    if (i == "A" || i == "a" || i == "E" || i == "e") {
      console.log("hello", i);
      count += 1;
    }
  }
  console.log(count);
}

let o = CountVowels("abcabc");
console.log("total vowels are", count);



function setUserName() {
    const myName = prompt("Please enter your name.");
    if (!myName) {
      setUserName();
    } else {
      localStorage.setItem("name", myName);
    }
  }

  
  setUserName()