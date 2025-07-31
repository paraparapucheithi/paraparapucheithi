
  document.addEventListener('DOMContentLoaded', function () {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.getElementById('navMenu');

    hamburger.addEventListener('click', function () {
      navMenu.classList.toggle('active');
    });
  });

