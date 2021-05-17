const tabs = document.getElementsByClassName('tabby');

function tabchange(Id){
	if(Id === "signup") {
        document.getElementsByClassName("signup")[0].style.display="block";
				document.getElementsByClassName("login")[0].style.display="None";

				tabs[1].classList.add('is-active');
        tabs[0].classList.remove('is-active');
	}
	if(Id === "login") {
        document.getElementsByClassName("login")[0].style.display="block";
				document.getElementsByClassName("signup")[0].style.display="None";

				tabs[0].classList.add('is-active');
        tabs[1].classList.remove('is-active');
	}
}



function checkRegValidity(form) {

    if(!form[0].checkValidity()){

        form[0].classList.add('exists');
        form[0].classList.add('is-danger');
        return false;

    }

    if(!form[1].checkValidity()){

        form[1].classList.add('exists');
        form[1].classList.add('is-danger');
        return false;

    }

    if(!form[2].checkValidity()){

        form[2].classList.add('exists');
        form[2].classList.add('is-danger');
        return false;

    }

    if(!form[3].checkValidity()){

        form[3].classList.add('exists');
        form[3].classList.add('is-danger');
        return false;

    }

    if(!(form[2].value===form[3].value)){

        form[3].classList.add('exists');
        form[3].classList.add('is-danger');
        return false;

    }


	return true;
}

function reEditReg(self){

    self.classList.remove('exists');
    self.classList.remove('is-danger');

}


function getOTP(self) {
	let form = document.forms[0];
	if (!checkRegValidity(form)) return false;

	self.classList.add('loader');

	let email = form.elements[0].value;
	console.log(email)
	fetch('/auth/isregistered?email=' + email)
	.then((response) => response.json())
	.then((data) => {
		if (data.otp) {
			self.classList.remove('loader');
			form.elements[7].value = data.otp;
			showNext();
		}
		else if (data.status) {
			self.classList.remove('loader');
			form.elements[0].classList.add(data.status);
			form.elements[0].classList.add('exists');
		}
	})
	.catch(console.error);
}


function showNext() {
	document.getElementsByClassName("icon-area")[0].style.display = 'none';
	document.getElementsByClassName("tabs")[0].style.display = 'none';
	document.getElementsByClassName("page-1")[0].style.display="none";
	document.getElementsByClassName("page-2")[0].style.display="block";
}
