function add(n1:number, n2:number){
    return n1 + n2;
}

console.log(add(1,3));

// ts void function

function greet(name:string):void {
    console.log('hello',name);
}

greet('jinal');

//typescript function
 // syntax
// function functionName(arg:argType){
//     '' function body
// }

// return type annotation

function add1(a:number, b:number):number{
    return a+b
}

console.log(add1(2,3))

// anonymous function -- an anonymous function is a nameless function defined at runtime and stored a variable.

const square=function(num:number):number{
    return num*num;
}

console.log(square(4));

// typescript functions type

// arrow function

const multi=(a:number, b:number):number => a*b;
console.log(multi(2,5))

// optional and default parameters in functions

function helo(fname:string,lname:string='lathiya'):string{
    return `hello ${fname} ${lname}`
}

console.log(helo('jinal'))
console.log(helo('jinal','lathiya'))


//rest parameters
// let var:string[];

function sum(...numbers:number[]):number{
    return numbers.reduce((acc,curr)=> acc+curr,0);
}
console.log(sum(1,2,3,4,5));


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

let value: number | string;
value="190"
console.log("numeric value"+value);
value="hello welcome"
console.log("string value"+value);


// types alias
/*  type alias give e new name.*/


/*  types in typescript are more flexible and can define primitive  intersection, union, tuple
while interface are used to describe the shape of an object. */

type type_alias = number | string | boolean;

let variable : type_alias;
variable=1;
console.log(variable);
variable="hello"
console.log(variable);
variable=true;
console.log(variable);


// enums

enum Carname{
    Honda,
    toyota,
    venue,
    I20
}

console.log(Carname)

let car=Carname.Honda;

console.log(car)

// typescript tuples

let arrTuple :[number,string]=[501,'hello'];
console.log(arrTuple)


interface abc {
    name:string
}

interface xyz extends  abc{
    age:number
}


let name="hello"