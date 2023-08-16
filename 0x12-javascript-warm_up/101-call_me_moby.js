#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  x = Math.abs(x);
  while (x) {
    theFunction();
    --x;
  }
};
