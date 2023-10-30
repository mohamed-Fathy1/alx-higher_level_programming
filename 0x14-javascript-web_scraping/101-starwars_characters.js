#!/usr/bin/node
// get status code

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id + '/';

request(url)
  .than((error, res, body) => {
    if (error) {
      console.error('error:', error);
    }
    const characters = JSON.parse(body).characters;
    console.log(characters);
    return characters;
  })
  .then(characters => Promise.all(characters.map(char => request(char))))
  .then(characters => characters.map(char => JSON.parse(char.body).name))
  .then(names => names.forEach(name => console.log(name)));
