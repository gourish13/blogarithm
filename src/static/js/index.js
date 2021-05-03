(function (){
  window.onload = function() {
    let nav = document.getElementsByTagName('nav')[0];
    window.onscroll = function() {
      let scrollVal = window.pageYOffset;
      if (scrollVal === 0)
        nav.classList = ['nav-hidden'];
      else if (scrollVal <= window.innerHeight && scrollVal > 0 && !nav.classList.contains('nav-transparent'))
        nav.classList = ['nav-transparent'];
      else if (scrollVal > window.innerHeight)
        nav.classList = [];
    }
  }
})();

