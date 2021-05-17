(function (){
  window.onload = function() {
    const nav = document.getElementsByTagName('nav')[0];
    const header = document.getElementsByClassName('header')[0];
    const arrow = document.getElementsByClassName('arrow-container')[0];
    window.onscroll = function() {
      let scrollVal = window.pageYOffset;
      arrow.classList.add('hide-arrow-container');
      if (scrollVal === 0) {
        arrow.classList.remove('hide-arrow-container');
        nav.classList = ['nav-hidden'];
      }
      else if (scrollVal <= header.clientHeight && scrollVal > 0 && !nav.classList.contains('nav-transparent'))
        nav.classList = ['nav-transparent'];
      else if (scrollVal > header.clientHeight)
        nav.classList = [];
    }
  }
})();

