const header = document.querySelector('#header');
const burger = document.querySelector('.burger');
const headerNav = document.querySelector('#header-nav');

const navSocial = document.querySelector('#nav-social');

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
  if(headerNav.classList.contains('left-0')) {
    headerNav.classList.remove('left-0');
    headerNav.classList.add('-left-full');
    navSocial.classList.remove('flex');
    navSocial.classList.add('hidden');
  }else{
    headerNav.classList.remove('-left-full');
    headerNav.classList.add('left-0');
    navSocial.classList.remove('hidden');
    navSocial.classList.add('flex');
  }
});