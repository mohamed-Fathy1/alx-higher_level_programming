#!/usr/bin/node
// get status code

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

function printCharacters (characters, i) {
  request.get(character[i], (error, res, body) => {
    if (error) {
      console.error('error:', error);
    }
    console.log(JSON.parse(body).name);
    if (i + 1 < characters.length) {
      printCharacters(characters, i + 1);
    }
  });
}

request.get(url, (error, res, body) => {
  if (error) {
    console.error('error:', error);
  }
  const characters = JSON.parse(body).characters;
  printCharacters(characters, 0);
});
