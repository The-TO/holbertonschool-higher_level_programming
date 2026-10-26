#!/usr/bin/node

const nbrArgs = process.argv.length - 2;

if (nbrArgs === 0) {
    console.log ('No argument');
} else if (nbrArgs === 1) {
    console.log ('Argument found');
} else {
    console.log ('Arguments found');
}
