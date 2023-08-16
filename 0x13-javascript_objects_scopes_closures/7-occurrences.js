#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const arr = list.filter(item => item === searchElement);
  return arr.length;
};
