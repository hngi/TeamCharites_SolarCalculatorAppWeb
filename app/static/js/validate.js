function validate() {
	let regex = /\W+/;
	let username = document.getElementById("username");
	let password = document.getElementById("password");
	let confirmPassword = document.getElementById("confirmPassword");

	let uppercase = /[A-Z]+/;
	let lowercase = /[a-z]+/;
	let numeric = /[0-9]+/;
	let symbols = /[\|!@#%-&\(\)_\+=\[\]{};\$'\*:"\\,\.<>\/\?`~£€\^ ]/;

	document.getElementById("usernameErrorMessage").innerHTML = "";
	document.getElementById("passwordErrorMessage").innerHTML = "";
	document.getElementById("confirmPasswordErrorMessage").innerHTML = "";

	if(username.value === "" || regex.test(username.value) === true  || username.value.length < 5 ) {
		document.getElementById("usernameErrorMessage").innerHTML = "Username should be a combination of lowercase and uppercase alphabetic characters, numeric characters and underscore";
		event.preventDefault();
	} else if(password.value === "" || uppercase.test(password.value) === false || lowercase.test(password.value) === false || numeric.test(password.value) === false || symbols.test(password.value) === false || !(password.value.length >= 5 && password.value.length <= 20) ) {
		    document.getElementById("passwordErrorMessage").innerHTML = "Password must be 5 to 20 characters long and must contain uppercase alphabetic character(s), lowercase alphabetic character(s), numeric character(s) and symbol(s)";
		    event.preventDefault();
	} else {
		if(password.value !== confirmPassword.value) {
			document.getElementById("confirmPasswordErrorMessage").innerHTML = "Your password don't match";
			event.preventDefault();
		}
	}
}
