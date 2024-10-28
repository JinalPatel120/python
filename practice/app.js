function add(n1, n2) {
    return n1 + n2;
}
console.log(add(1, 3));
// ts void function
function greet(name) {
    console.log('hello', name);
}
greet('jinal');
//typescript function
// syntax
// function functionName(arg:argType){
//     '' function body
// }
// return type annotation
function add1(a, b) {
    return a + b;
}
console.log(add1(2, 3));
// anonymous function -- an anonymous function is a nameless function defined at runtime and stored a variable.
var square = function (num) {
    return num * num;
};
console.log(square(4));
// typescript functions type
// arrow function
var multi = function (a, b) { return a * b; };
console.log(multi(2, 5));
// optional and default parameters in functions
function helo(fname, lname) {
    if (lname === void 0) { lname = 'lathiya'; }
    return "hello ".concat(fname, " ").concat(lname);
}
console.log(helo('jinal'));
console.log(helo('jinal', 'lathiya'));
//rest parameters
// let var:string[];
function sum() {
    var numbers = [];
    for (var _i = 0; _i < arguments.length; _i++) {
        numbers[_i] = arguments[_i];
    }
    return numbers.reduce(function (acc, curr) { return acc + curr; }, 0);
}
console.log(sum(1, 2, 3, 4, 5));
// callback function
// callback function that can be passes as an argument to another function
// and is executed when a specific event or task is completed.
//typescript unknown functions
/*
in typescript the unknown type is used for variables whose types aren't known in advance.
gfg - represents the name of function
input- name of the parameter passed to the function
unknown - type of parameter passed
void- represents the return type of the function
*/
// use unknown enforces type checks and assertions, leading to safer and more 
// predictable code.
// typescript Union
/*
in typescript we can combine 1 or 2 different types of data.
*/
var value;
value = "190";
console.log("numeric value" + value);
value = "hello welcome";
console.log("string value" + value);
var variable;
variable = 1;
console.log(variable);
variable = "hello";
console.log(variable);
variable = true;
console.log(variable);
// enums
var Carname;
(function (Carname) {
    Carname[Carname["Honda"] = 0] = "Honda";
    Carname[Carname["toyota"] = 1] = "toyota";
    Carname[Carname["venue"] = 2] = "venue";
    Carname[Carname["I20"] = 3] = "I20";
})(Carname || (Carname = {}));
console.log(Carname);
var car = Carname.Honda;
console.log(car);
// typescript tuples
var arrTuple = [501, 'hello'];
console.log(arrTuple);
