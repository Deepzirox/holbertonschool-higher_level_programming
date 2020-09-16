#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 1 || num === 0) {
    return 1;
  }
  return factorial(num - 1) * num;
}

const n = parseInt(process.argv[2]);
console.log(factorial(n));
