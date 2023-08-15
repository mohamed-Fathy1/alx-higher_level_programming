#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const arr = process.argv.slice(2);
  arr.sort();
  const newArr = [];
  for (const x in [...arr]) {
    newArr[x] = Number(arr[x]);
  }
  const maxVal = Math.max(...newArr);
  console.log(newArr[newArr.indexOf(maxVal) - 1]);
}
