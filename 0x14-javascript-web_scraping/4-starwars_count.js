#!/usr/bin/node
// get status code

const request = require('request');

const url = process.argv[2];

request.get(url, (error, res, body) => {
  if (error) {
    console.error('error:', error);
  }
  const films = JSON.parse(body);
  let count = 0;
  films.forEach((film) => {
    const characters = film.characters;
    characters.forEach((character) => {
      if (character.includes('18')) {
        count++;
      }
    });
  });
  console.log(count);
});
