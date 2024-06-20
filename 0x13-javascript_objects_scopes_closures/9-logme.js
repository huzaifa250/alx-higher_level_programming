#!/usr/bin/node
let count = 0; // count the number of times logMe function is called.

exports.logMe = function (item) {
  console.log(count + ': ' + item);
  count++;
};
