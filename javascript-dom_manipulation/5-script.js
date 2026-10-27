const header = document.querySelector('header');
const update = document.querySelector('#update_header');

update.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
