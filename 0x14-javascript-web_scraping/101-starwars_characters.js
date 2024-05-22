#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = JSON.parse(body);
    const characters = content.characters;
    
    const getCharacterName = (characterUrl) => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            const character = JSON.parse(body);
            resolve(character.name);
          }
        });
      });
    };

    const fetchCharacters = async () => {
      for (const character of characters) {
        try {
          const name = await getCharacterName(character);
          console.log(name);
        } catch (error) {
          console.log(error);
        }
      }
    };

    fetchCharacters();
  }
});
