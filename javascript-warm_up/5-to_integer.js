#!/usr/bin/node

const isInt = parseInt(process.argv[2]);

if (isNaN(isInt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + isInt);
}
