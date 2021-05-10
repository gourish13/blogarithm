const tabs = documents.getElementByClassName('tabby')

function showNext(){
	document.getElementsByClassName("page-1")[0].style.display="None";
	document.getElementsByClassName("page-2")[0].style.display="block";
}
function tabchange(Id){
	if(Id == "signup"){
        document.getElementsByClassName("signup")[0].style.display="block";
		document.getElementsByClassName("login")[0].style.display="None";

		tabs[1].classList = ['is-active' , 'tabby'];
        tabs[0].classList = ['tabby']
	}
	if(Id == "login"){
        document.getElementsByClassName("login")[0].style.display="block";
		document.getElementsByClassName("signup")[0].style.display="None";

		tabs[0].classList = ['is-active' , 'tabby'];
        tabs[1].classList = ['tabby'];
	}
}
