(function (){
  window.onload = function() {
    const nav = document.getElementsByTagName('nav')[0];
    const header = document.getElementsByClassName('header')[0];
    window.onscroll = function() {
      let scrollVal = window.pageYOffset;
      if (scrollVal === 0)
        nav.classList = ['nav-hidden'];
      else if (scrollVal <= header.clientHeight && scrollVal > 0 && !nav.classList.contains('nav-transparent'))
        nav.classList = ['nav-transparent'];
      else if (scrollVal > header.clientHeight)
        nav.classList = [];
    }
  }
})();

