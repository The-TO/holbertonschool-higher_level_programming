const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
const listMovies = document.querySelector('#list_movies');

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    data.results.forEach((film) => {
      const item = document.createElement('li');
      item.textContent = film.title;
      listMovies.appendChild(item);
    });
  })
  .catch((error) => {
    console.error('Error:', error);
  });
