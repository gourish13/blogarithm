function createblog()
{
	var myform = document.getElementById("myform");
	var title = document.getElementById("blog-title").value.trim() ;
	var content = simplemde.value().trim();
	console.log() ; 
	if(title === '')
		document.getElementById("error").innerHTML = "Title Cannot be empty" ; 
	else if(content === '')
		document.getElementById("error").innerHTML = "Empty Blog cannot be published" ; 
	else
	{
		if(document.getElementById("bswitch").checked)
		document.getElementById("private").value = "false"
		
		myform.submit()
	}
}