var tabs = document.getElementsByClassName('tabby');

function showNext(){
	document.getElementsByClassName("page-1")[0].style.display="None";
	document.getElementsByClassName("page-2")[0].style.display="block";
}
function tabchange(Id){
	console.log(tabs)
	if(Id === "signup"){
        document.getElementsByClassName("signup")[0].style.display="block";
		document.getElementsByClassName("login")[0].style.display="None";

		tabs[1].classList.add('is-active');
        tabs[0].classList.remove('is-active');
	}
	if(Id === "login"){
        document.getElementsByClassName("login")[0].style.display="block";
		document.getElementsByClassName("signup")[0].style.display="None";

		tabs[0].classList.add('is-active');
        tabs[1].classList.remove('is-active');
	}
	console.log(tabs)
}
