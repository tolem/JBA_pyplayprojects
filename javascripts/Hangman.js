const prompt= require("prompt-sync")({sigint: true})

// Use "input()" to input a line from the user
// Use "input(str)" to print some text before requesting input
// You will need this in the following stages
//const input = require('sync-input')
let win = 0;
let loss = 0;
console.log(`H A N G M A N`);
let start = true;
//console.log(`--------`);
while( start == true) {
    let demand = prompt('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if (demand == 'play') {

const words = ["python", "java", "swift", "javascript"];

const word = words[Math.floor(Math.random() * 4)];

const wordpeek = "-".repeat(word.length).split('');
//const userInput = input(`Guess the word ${wordpeek}: \n`);

const splitingWord = word.split('');

let checker = [];

const letters = 'abcdefghijklmnopqrstuvwxyz'

let attempts = 8;


while (attempts){

  if (wordpeek.join('') === word) {
      win += 1;  
      console.log(`\nYou guessed the word ${wordpeek.join('')}! \nYou survived!`); break;
    };
  
  console.log(`${wordpeek.join('')}`); 
  
  let userChoice = prompt (`Input a letter: //${attempts} attempts `);
  
  if (userChoice.length > 1 || userChoice.length < 1){console.log(`Please, input a single letter.`)
  } else if (!letters.includes(userChoice)){console.log(`Please, enter a lowercase letter from the English alphabet.`)}
  else { let indices = [];
  
        let idx = splitingWord.indexOf(userChoice)
  
        if(!checker.includes(userChoice)) {
           checker.push(userChoice)
    
          if(word.includes(userChoice)) {
            while (idx !== -1) {
            indices.push(idx)
            idx = splitingWord.indexOf(userChoice, idx + 1);
              }
            indices.forEach(el => wordpeek[el] = userChoice);
            } else {
              console.log(`That letter doesn't appear in the word.`);
              attempts -= 1;
            }
          } else {
            console.log(`You've already guessed this letter.`)
  
    }
  if (attempts == 0) {
    loss += 1;
    console.log(`\nYou lost!`);
        }
    }   
}
    } else if ( demand == 'results') {
        console.log(`You won: ${win} times.\nYou lost: ${loss} times.`)
    } else if (demand == 'exit') {
        start = false
    }
}
