#!/usr/bin/node
// get status code

const request = require('request');

request.get('https://swapi-api.alx-tools.com/api/people/18/', (error, res, body) => {
  if (error) {
    console.error('error:', error);
  }
  const title = JSON.parse(body).films.length;
  console.log(title);
});
