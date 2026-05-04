const header = document.querySelector('#header');
const burger = document.querySelector('.burger');
const headerNav = document.querySelector('#header-nav');

window.addEventListener('scroll', () => {
  if (window.scrollY > 64) {
    header.classList.add('bg-black');
    header.classList.remove('bg-transparent');
  } else {
    header.classList.add('bg-transparent');
    header.classList.remove('bg-black');
  }
});

burger.addEventListener('click', () => {
  burger.classList.toggle('opened');
  if(headerNav.classList.contains('right-0')) {
    headerNav.classList.remove('right-0');
    headerNav.classList.add('-right-full');
  }else{
    headerNav.classList.remove('-right-full');
    headerNav.classList.add('right-0');
  }
});