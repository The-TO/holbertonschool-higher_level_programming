const header = document.querySelector('header');
const btn = document.querySelector('#toggle_header');

btn.addEventListener('click', () => {
    if (header.classList.contains('red')){
        header.classList.toggle('red')
        header.classList.add('green')
    } else {
        header.classList.toggle('green')
        header.classList.add('red')
    }
});