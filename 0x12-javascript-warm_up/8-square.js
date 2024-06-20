#!/usr/bin/node
/* parses the third command-line argument as a number,
converts it to an integer using Math.floor */
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let ro = 0; ro < size; ro++) {
    let row = '';
    for (let i = 0; i < size; i++) row += 'X';
    console.log(row);
  }
}
