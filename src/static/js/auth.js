resend = (function(){

    let count = 2;

    return function(self , a){

        if(count > 0){

            self.innerHTML = `Resend <span class="loader"></span>`;
            count--;
            emailid = self.form.elements['email'].value
            let url = "";
            if(a===0)
                url = "/auth/otp/resend?email=";
            else
                url = "/auth/resend-password?email="

            fetch(url + emailid)
                    .then(function(data) {return data.json();})
                    .then(function(data){

                        self.form.elements['hashed-otp'].value = data['otp'];
                        self.innerHTML = `Resend(${count})`;
                        if(count === 0) self.disabled = true;

                    })
                    .catch(function(err) {throw err;})

        }
    
    }
    
})();

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
        document.getElementById('warn').innerHTML = "Passwords does not match";
        return false;

    }


	return true;
}

function reEditReg(self){

    self.classList.remove('exists');
    self.classList.remove('is-danger');

}


function getOTP(self) {
    document.getElementById('warn').innerHTML = '';
	let form = document.forms[0];
	if (!checkRegValidity(form)) return false;

	self.classList.add('loader');

	let email = form.elements[0].value;
	fetch('/auth/otp/send?email=' + email)
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
            document.getElementById('warn').innerHTML = "Email Id is already registered";
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

function sendresetotp()
{
	document.getElementById("reset-otp").style.display = "block";
	document.getElementById("newpassword").style.display = "block";
	document.getElementById("confirmpassword").style.display = "block";
	document.getElementById("save").style.display = "block";
	
	document.getElementById("email").style.display = "none";
	document.getElementById("send_otp").style.display = "none";
	
}

function enable()
{
	document.getElementsByClassName("modal")[0].classList.add("is-active");
	
}


function disable()
{
	
	document.getElementById("reset-otp").style.display = "none";
	document.getElementById("newpassword").style.display = "none";
	document.getElementById("confirmpassword").style.display = "none";
	document.getElementById("save").style.display = "none";
	
	document.getElementById("email").style.display = "block";
	document.getElementById("send_otp").style.display = "block";
	document.getElementById("send_otp").style.display = "block";
	
	document.getElementsByClassName("modal")[0].classList.remove("is-active");
	
}

