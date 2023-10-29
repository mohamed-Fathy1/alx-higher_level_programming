#!/usr/bin/node
// get status code

const request = require('request');

const id = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${id}`, (error, res, body) => {
  if (error) {
    console.error('error:', error);
  }
  console.log(res);
});
