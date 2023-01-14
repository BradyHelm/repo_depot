// Object Destructuring 1
// What does the following code return/print?

let facts = {numPlanets: 8, yearNeptuneDiscovered: 1846};
let {numPlanets, yearNeptuneDiscovered} = facts;

console.log(numPlanets); // ? returns 8
console.log(yearNeptuneDiscovered); // returns 1846



// Object Destructuring 2
// What does the following code return/print?

let planetFacts = {
  numPlanets: 8,
  yearNeptuneDiscovered: 1846,
  yearMarsDiscovered: 1659
};

let {numPlanets, ...discoveryYears} = planetFacts;

console.log(discoveryYears); //{1846, 1659}



// Object Destructuring 3
// What does the following code return/print?

function getUserData({firstName, favoriteColor="green"}){
  return `Your name is ${firstName} and you like ${favoriteColor}`;
}

getUserData({firstName: "Alejandro", favoriteColor: "purple"}) // ? firstName: "Alejandro", favoriteColor: "purple"
getUserData({firstName: "Melissa"}) // ?firstName: "Melissa", favoriteColor: undefined
getUserData({}) // ?  firstName: "Alejandro", favoriteColor: "purple"


// Array Destructuring 1
// What does the following code return/print?

let [first, second, third] = ["Maya", "Marisa", "Chi"];

console.log(first); // "Maya"
console.log(second); // "Marisa"
console.log(third); // "Chi"

// Array Destructuring 2
// What does the following code return/print?

let [raindrops, whiskers, ...aFewOfMyFavoriteThings] = [
  "Raindrops on roses",
  "whiskers on kittens",
  "Bright copper kettles",
  "warm woolen mittens",
  "Brown paper packages tied up with strings"
]

console.log(raindrops); // ?   "Raindrops on roses",
console.log(whiskers); // ?   "whiskers on kittens",
console.log(aFewOfMyFavoriteThings); // ? ["Bright copper kettles", "warm woolen mittens","Brown paper packages tied up with strings"]


// Array Destructuring 3
// What does the following code return/print?

let numbers = [10, 20, 30];
[numbers[1], numbers[2]] = [numbers[2], numbers[1]]

console.log(numbers) //  [10, 30, 20]

// ES5 Assigning Variables to Object Properties
var obj = {
  numbers: {
    a: 1,
    b: 2
  }
};

var a = obj.numbers.a;
var b = obj.numbers.b;

// ES2015 Object Destructuring
const { a, b } = obj

// ES5 Array Swap
var arr = [1, 2];
var temp = arr[0];
arr[0] = arr[1];
arr[1] = temp;
// ES2015 One-Line Array Swap with Destructuring
[1, 2] = [2, 1];


let names = ['Tom', 'Margaret', 'Allison', 'David', 'Pierre']
const raceResults = (arr) => {
    [first, second, third, ...Rest ] = arr;
    return raceResults;
}
