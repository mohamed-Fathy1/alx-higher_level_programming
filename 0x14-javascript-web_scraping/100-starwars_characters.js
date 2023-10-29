#!/usr/bin/node
// get status code

const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request.get(url, (error, res, body) => {
  if (error) {
    console.error('error:', error);
  }
  const characters = JSON.parse(body).characters;
  characters.forEach((character) => {
    request.get(character, (error, res, body) => {
      if (error) {
        console.error('error:', error);
      }
      console.log(JSON.parse(body).name);
    });
  });
});
