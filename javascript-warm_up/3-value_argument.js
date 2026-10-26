#!/usr/bin/node

const nbrArgs = process.argv[2];

if (nbrArgs >= 2) {
  console.log(nbrArgs);
} else {
  console.log('No argument');
}
