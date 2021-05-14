function createblog() {
	let myform = document.getElementById("myform");
	let title = document.getElementById("blog-title").value.trim() ;
	let content = simplemde.value().trim();

	if(title === '') {
		document.getElementById("error").innerHTML = "Title Cannot be empty" ;
		return false; 
	}
	if(content === '') {
		document.getElementById("error").innerHTML = "No content to publish" ; 
		return false;
	}

	document.getElementById("private").value = document.getElementById("bswitch").checked;
	myform.submit();
}