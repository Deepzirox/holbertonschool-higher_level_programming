#!/usr/bin/node

exports.esrever = function (list) {
  let long = list.length - 1;

  for (let i = 0; i < long; i++, long--) {
    const tmp = list[i];
    list[i] = list[long];
    list[long] = tmp;
  }
  return list;
};
