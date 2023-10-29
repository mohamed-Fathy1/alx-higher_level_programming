#!/usr/bin/node
// Script that computes the number of tasks completed by user id.

const request = require('request');

const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  const todos = JSON.parse(body);
  const completed = {};
  for (const todo of todos) {
    if (todo.completed === true) {
      if (completed[todo.userId] === undefined) {
        completed[todo.userId] = 1;
      } else {
        completed[todo.userId] += 1;
      }
    }
  }
  console.log(completed);
}
);
