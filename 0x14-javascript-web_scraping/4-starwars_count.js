#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const wedge = 18;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let count = 0;
    for (const film of data) {
      for (const character of film.characters) {
        if (character.includes(wedge)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
