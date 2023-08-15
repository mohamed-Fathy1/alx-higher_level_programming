#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  process.argv.sort();
  console.log(process.argv[process.argv.length - 2]);
}
