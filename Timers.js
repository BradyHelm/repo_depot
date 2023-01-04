

// function countDown(time){
//     let intTimer = setInterval(function(){
//         time--;
//         if(time <= 0){
//             clearInterval(intTimer);
//             console.log('DONE!')
//         }
//         else 
//             console.log(time)
//         },1000)
     
function randomGame(){

    let tries = 0;
    
    let num;

    let intTimer = setInterval(() => {

        let num = Math.random();

            tries++;

            if (num > .75) {

                clearInterval(intTimer);

                console.log('Number of tries:' + tries);

            };

            

    }, 1000);
  
};

console.log(randomGame());




  

