(function (){
  window.onload = function() {
    let nav = document.getElementsByTagName('nav')[0];
    window.onscroll = function() {
      let scrollVal = window.pageYOffset;
      if (scrollVal === 0)
        nav.classList = ['nav-hidden'];
    }
  }
})();

