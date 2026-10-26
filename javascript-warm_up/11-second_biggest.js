#!/usr/bin/node
const nums = process.argv.slice(2).map((arg) => parseInt(arg));

if (nums.length < 2) {
  console.log(0);
} else {
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}
