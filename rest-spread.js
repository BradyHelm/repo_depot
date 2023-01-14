const filterOutOdds = (...arr) => {
return arr.filter(num => num % 2 ===0);
}




const mergeObjects = (one, two) => {
    let newObj = {...one, ...two}
     return newObj;
}

const findMin = (...val) => Math.min (...val);


const doubleAndReturnArgs = (arr, ...addVals) => {
 result = [...arr, ...addVals.map(val => val * 2)];
    
 return result;
}






/** remove a random element in the items array
and return a new array without that item. */

function removeRandom(items) {

}

/** Return a new array with every item in array1 and array2. */

const extend = (array1, array2) => {
    let newArr = [...array1, ...array2];

    return newArr;

}

/** Return a new object with all the keys and values
from obj and a new key/value pair */

const addKeyVal = (obj, key, val) => {
let newObj = {...obj}  
newObj[key] = val;
return newObj;
}


/** Return a new object with a key removed. */

const removeKey = (obj, key) => {
    let delObj = {...obj}
    delete delObj[key];
    return delObj;

}


/** Combine two objects and return a new object. */

const combine = (obj1, obj2) => {
    newObj = {...obj1, ...obj2}
    return newObj;
}


/** Return a new object with a modified key and value. */

const update = (obj, key, val) => {
 let newObj = {...obj};
 obj[key] = val;
 return newObj;  

}