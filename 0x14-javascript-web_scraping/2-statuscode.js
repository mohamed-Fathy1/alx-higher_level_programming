#!/usr/bin/node
// get status code

const request = require('request');

const url = process.argv[2];

request.get(url, (error, res, body) => {
  console.log('code: ' + res.statusCode);
});
