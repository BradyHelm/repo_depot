// categories is the main data structure for the app; it looks like this:

//  [
//    { title: "Math",
//      clues: [
//        {question: "2+2", answer: 4, showing: null},
//        {question: "1+1", answer: 2, showing: null}
       
//      ],
//    },
//    { title: "Literature",
//      clues: [
//        {question: "Hamlet Author", answer: "Shakespeare", showing: null},
//        {question: "Bell Jar Author", answer: "Plath", showing: null},
//        ...
//      ],
//    },
//    ...
//  ]

let categories = [];

const NUM_CATEGORIES = 6
const NUM_QUESTIONS_PER_CAT = 5
/** Get NUM_CATEGORIES random category from API.
 
 * Returns array of category ids
 */


async function getCategoryIds(catId) {
    let response = await axios.get('https://jservice.io/api/categories?count=100');
    if(response.status === 200) {
        let catIds = response.data.map(e => e.id);
        console.log(catIds)
        return catIds.slice().sort(() => Math.random() - 0.5).slice(0, 5);
    }else{
        throw new Error('Error while fetching data')
    }
};

   
/** Return object with data about a category:
 *
 *  Returns { title: "Math", clues: clue-array }
 *
 * Where clue-array is:
//  *   [
 *      {question: "Hamlet Author", answer: "Shakespeare", showing: null},
 *      {question: "Bell Jar Author", answer: "Plath", showing: null},
 *      ...
 *   ]
 */

const NUM_CLUES_PER_CAT = 5;
async function getCategory(catId) {
let response = await axios.get(`https://jservice.io/api/category?id=${catId}`);
let cat = response.data;
let allClues = cat.clues;
const cluesRandom = allClues.slice().sort(() => Math.random() - 0.).slice(0, 5);
let clues = cluesRandom.map(e => ({
    question: e.question,
    answer: e.answer,
    showing: null,
    }));
    console.log(clues)
  return { title: cat.title, clues };
  
}





/** Fill the HTML table#jeopardy with the categories & cells for questions.
 *
 * - The <thead> should be filled w/a <tr>, and a <td> for each category
 * - The <tbody> should be filled w/NUM_QUESTIONS_PER_CAT <tr>s,
 *   each with a question for each category in a <td>
 *   (initally, just show a "?" where the question/answer would go.)
 */
  
  let catRow = document.querySelector('thead')
  let grid = document.querySelector('tbody')
  let catCell = document.createElement('th')
  let clueRow = document.createElement('tr')
  let clueCell = document.createElement('td')
 

async function fillTable() {
    let table = document.querySelector('#jeopardy');
   table.innerHTML ='';
   let clueRow = document.createElement('tr');
   for (let i = 0; i < 5; i++) {
    let catCell = document.createElement('th');
    catCell.textContent = categories[i];
    console.log(categories[i])
    clueRow.append('th');
   
    let catRow = document.querySelector('thead')
    catRow.append('tr');
    }


   table.innerHTML = '';
   for(let j = 0; j < 5 ; j++) {
    for(let k = 0; k < 5; k++) {
        clueCell.id =`${j}-${k}`; 
        clueCell.innerHTML = '?'; 
    }
 table.append(clueRow);
   }   
 
}


/** Handle clicking on a clue: show the question or answer.
 *
 * Uses .showing property on clue to determine what to show:
 * - if currently null, show question & set .showing to "question"
 * - if currently "question", show answer & set .showing to "answer"
 * - if currently "answer", ignore click
 * */

// 

function handleClick(evt) {
    let target = evt.target;
    let id = target.id;
    let catId = id.split('-')[0];
    let clueId = id.split('-')[1];
    let clue = categories[catId].clues[clueId];
    
    if (clue.showing === 'question') {
        target.innerText = clue.question;
        clue.showing = 'answer';
    } else if (clue.showing === 'answer') {
        target.innerText = '?';
        clue.showing = 'question';
    }
}

let cells = document.querySelectorAll('#jeopardy tbody td');
cells.forEach(cell => cell.addEventListener('click', handleClick));

/** Wipe the current Jeopardy board, show the loading spinner,
 * and update the button used to fetch data.
 */

function showLoadingView() {
   
}

/** Remove the loading spinner and update the button used to fetch data. */
const spinner = document.querySelector("#spin-container")
function hideLoadingView() {
    spinner.value = '';
    start.append.innerHTML("Reload")
}

/** Start game:
 *
 * - get random category Ids
 * - get data for each category
 * - create HTML table
 * */

async function setupAndStart() {
    let catIds = await getCategoryIds();
    let categoriesPromises = catIds.map(catId => getCategory(catId));
    categories = await Promise.all(categoriesPromises);
  }

   fillTable();


/** On click of start / restart button, set up game. */
const start = document.querySelector("#start");
start.addEventListener('click', setupAndStart);
/** On page load, add event handler for clicking clues */
document.addEventListener('DOMContentLoaded', () => {
    
    setupAndStart();
    document.getElementById('jeopardy').addEventListener('click', handleClick);

});

// `<thead>
// <tr>
//     <th>"Cat Title Goes Here"</th>
//     <th>"Cat Title Goes Here"</th>
//     <th>"Cat Title Goes Here"</th>
//     <th>"Cat Title Goes Here"</th>
//     <th>"Cat Title Goes Here"</th>
//     <th>"Cat Title Goes Here"</th>
// </tr>
// </thead>
// <tbody>
// <tr>
//     <td id= "0-0">?</td>
//     <td id= "1-0">?</td>
//     <td id= "2-0">?</td>
//     <td id= "3-0">?</td>
//     <td id= "4-0">?</td>
//     <td id= "5-0">?</td>
// </tr>
// <tr>
//     <td id= "0-1">?</td>
//     <td id= "1-1">?</td>
//     <td id= "2-1">?</td>
//     <td id= "3-1">?</td>
//     <td id= "4-1">?</td>
//     <td id= "5-1">?</td>
// </tr>
// <tr>
//     <td id= "0-2">?</td>
//     <td id= "1-2">?</td>
//     <td id= "3-2">?</td>
//     <td id= "4-2">?</td>
//     <td id= "5-2">?</td>
//     <td id= "6-2">?</td>
// </tr>
// <tr>
//     <td id= "0-3">?</td>
//     <td id= "1-3">?</td>
//     <td id= "2-3">?</td>
//     <td id= "3-3">?</td>
//     <td id= "4-3">?</td>
//     <td id= "5-3">?</td>
// </tr>
// <tr>
//     <td id= "0-4">?</td>
//     <td id= "1-4">?</td>
//     <td id= "2-4">?</td>
//     <td id= "3-4">?</td>
//     <td id= "4-4">?</td>
//     <td id= "5-4">?</td>
// </tr>
// </tbody>`