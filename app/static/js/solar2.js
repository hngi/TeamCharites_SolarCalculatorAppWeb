let total1 = 0;
function calculate() {
	let array = ["device","quantity","power","hoursPerDay","wattsPerDevice"];
	let device = document.getElementById(array[0]).value;
	let quantity = document.getElementById(array[1]).value;
	let power = document.getElementById(array[2]).value;
	let hoursPerDay = document.getElementById(array[3]).value;

	if (device == "" || quantity == "" || power == "" || hoursPerDay == "") {
		alert("Please input your values");
	}else if(!isNaN(device)) {
		alert("Enter name of appliance in first column");
		for (let i = 0; i <= 4; i++){
		    document.getElementById(array[i]).value = "";
		}
	} else if (isNaN(quantity) || isNaN(power) || isNaN(hoursPerDay)){
		alert("Wrong input, enter digits in the second, third and fourth coulmn");
		for (let i = 0; i <= 4; i++){
		    document.getElementById(array[i]).value = "";
		}
	}
	else {
		let tr = document.getElementById("theTable");
	    let row = tr.insertRow(0);
	    let total = 1;
	    for (let i = 0; i < 5; i++) {
		    if (i == 4) {
			    let b = row.insertCell(i);
			    b.innerHTML = total;
			    deleteButton(row);
			    break;
		    } else {
		        let b = row.insertCell(i);
		        b.innerHTML = document.getElementById(array[i]).value;
		        if (!isNaN(b.innerHTML)) {
		            total *= b.innerHTML;
		        }
		        document.getElementById(array[i]).value = "";
	        }
	    }
	    total1 += parseInt(total);
    }
    console.log(theTable);
}

function totalPowerConsumption() {
	let show = document.getElementById("total");
	show.innerHTML = total1;
	show.style.display = "block";
	total1 = 0;
}

function deleteButton(aRow) {
	aDeleteButton = document.createElement("button");
	aDeleteButton.classList.add("newButton");
	aDeleteButton.innerHTML = "delete";
    aRow.appendChild(aDeleteButton);
}

function reset() {
	let b = document.getElementById("theTable")
	while(b.hasChildNodes()) {
		b.removeChild(b.lastChild);
	}
	document.getElementById("total").innerHTML = "";
	total1 = 0;

}





