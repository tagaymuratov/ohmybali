const header = document.querySelector('#header');

window.addEventListener('scroll', () => {
  if (window.scrollY > 64) {
    header.classList.add('bg-black');
    header.classList.remove('bg-transparent');
  } else {
    header.classList.add('bg-transparent');
    header.classList.remove('bg-black');
  }
});