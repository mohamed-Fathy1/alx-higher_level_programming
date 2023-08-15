#!/usr/bin/node

function add (a, b) {
  console.log(a + b);
}

const firstArg = process.argv[2];
const secondArg = process.argv[3];

if (Number(firstArg) && Number(secondArg)) { add(firstArg, secondArg); } else { console.log(NaN); }
