import arr from 'arr';
[ 2, 3, 6, 78, 99, 104, 23 ].reduce((max, currNum) => {
   return Math.max(max, currNum);
});



// ES2015 Arrow Functions Shorthand
 let double = arr => arr.map((val) => val * 2); 

 
  let squareAndFindEvens = numbers => {
    let squares = numbers.map((num) => {
      return num ** 2;
    });

    let evens = squares.filter((square) =>{
      return square % 2 === 0;
    });
    return evens; 
  }
  