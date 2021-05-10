function next(){
	document.getElementsByClassName("page-1")[0].style.display="None";
	document.getElementsByClassName("page-2")[0].style.display="block";
}
function tabchange(Id){
	if(Id == "signup"){
		document.getElementsByClassName("signup")[0].style.display="block";
		document.getElementsByClassName("login")[0].style.display="None";
	}
	if(Id == "login"){
		document.getElementsByClassName("login")[0].style.display="block";
		document.getElementsByClassName("signup")[0].style.display="None";
	}
}