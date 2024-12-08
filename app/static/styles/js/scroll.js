
  document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector('.navbar');

    window.addEventListener('scroll', function () {
      if (window.scrollY > 50) { // Adjust the value as needed
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    });
  });
