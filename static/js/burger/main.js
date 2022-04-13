const overlay = document.querySelector('.overlay');
const menu = document.querySelector('.right-menu');
const menuButton = document.querySelector('.burger-menu');
const menuClose = document.querySelector('.close-menu');

menuButton.addEventListener('click', () => {
    overlay.classList.add('is-active');
    menu.classList.add('is-active');
    menuClose.classList.add('is-active');
    document.body.style.overflow = 'hidden';
});

menuClose.addEventListener('click', () => {
    menuClose.classList.remove('is-active');
    overlay.classList.remove('is-active');
    menu.classList.remove('is-active');
    document.body.style.overflow = 'auto';
});

overlay.addEventListener('click', () => {
    menuClose.classList.remove('is-active');
    overlay.classList.remove('is-active');
    menu.classList.remove('is-active');
    document.body.style.overflow = 'auto';
});
