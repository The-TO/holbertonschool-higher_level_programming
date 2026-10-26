#!/usr/bin/node

const nbrArgs = process.argv[2];

if (nbrArgs === undefined){
  console.log('No argument');
} else {
  console.log(nbrArgs)
}
