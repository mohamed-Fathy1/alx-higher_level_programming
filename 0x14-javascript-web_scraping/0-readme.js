#!/usr/bin/node
// print the content of a file
const fs = require('fs');

const FILE_NAME = process.argv[1];

fs.readFile(FILE_NAME, 'utf8', (error, data) => {
  if (error) { console.log(error); } else { console.log(data); }
});
