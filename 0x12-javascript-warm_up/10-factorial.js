#!/usr/bin/node

function factorial (n) {
  if (!firstArg || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const firstArg = Number(process.argv[2]);
console.log(factorial(firstArg));
