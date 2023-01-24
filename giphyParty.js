// console.log("Let's get this party started!");

// async function getGiphy() {
//     const res = await axios.get('http://api.giphy.com/v1/gifs/search'); // post,
//     console.log(res.data);
//     const img = document.querySelector("TBD");
//     img.src = res.data.message;
// }
// async function makeGiphy() {
//     const url = `http://api.giphy.com/v1/gifs/${search}`;
//     const res = await axios.get(url);
//     const img = document.querySelector('TBD')
//     img.src = res.data.message;
// }
// const form = document.querySelector('#form');
// const input = document.querySelector('#search-box');
// form.addEventListener('submit', function (e) {
// e.preventDefault();
// makeGiphy(input.value);
// input.value = '';

// })

// images.original.url

// https://api.giphy.com/v1/gifs/search?q=hilarious&api_key=MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym


const fetchData = async (searchTerm) => {

    try {

        const response = await fetch(`https://api.giphy.com/v1/gifs/search?q=${searchTerm}&api_key=MhAodEJIJxQMxW9XqxKjyXfNYdLoOIym`);

        const {data} = await response.json();
        console.log(data); 
        return data;
        
    } catch (error) {

        console.error(error);

        throw new Error(error);
       
    };

};

const input = document.querySelector('#search-box');
const searchBtn = document.querySelector('#search-button');
const removeBtn = document.querySelector('#remove');
const imgContainer = document.querySelector('#image-container');

document.addEventListener('DOMContentLoaded', () => {
console.log("loaded")


searchBtn.addEventListener('click', async function() {
    // console.log("I just clicked search")


// Tbhis is for error handling
const searchTerm = input.value;
 if(!searchTerm.length){
 alert('Please enter a search term')

 return;
};

const results =  await fetchData(searchTerm);
if(!results.length){
    alert('No results found')
    return;
};
// this clears the input field
input.value = '';

// This creates a variable that selects a random giph from the search results
const randomIdx = Math.floor(Math.random() * results.length);
// this creates a new element from the path below.
const image = document.createElement('img')
image.src = results[randomIdx].images.original.url;
// This appends the image variable to the imgContainer.
imgContainer.appendChild(image);
// this clears the page and sets teh variable imgContainer to empty.
removeBtn.addEventListener('click', () => {
    imgContainer.innerHTML = '';

    });

   });
});


