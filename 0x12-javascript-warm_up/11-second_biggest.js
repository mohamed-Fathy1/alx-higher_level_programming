#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2).sort();

  for (const x of [...arr]) {
    arr.shift();
    arr.push(Number(x));
  }
  const maxVal = Math.max(...arr);
  console.log(arr[arr.indexOf(maxVal) - 1]);
}
