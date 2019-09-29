var rIndex,
total = 0,
table = document.getElementById("table");


// check the empty input
function checkEmptyInput()
{
    var isEmpty = false,
        d = document.getElementById("d").value,
        q = document.getElementById("q").value,
        p = document.getElementById("p").value,
        h = document.getElementById("h").value;

    if(d === ""){
        alert("Device Cannot Be Empty");
        isEmpty = true;
    }
    else if(q === ""){
        alert("Quantity Cannot Be Empty");
        isEmpty = true;
    }
    else if(p === ""){
        alert("Power Consumption Cannot Be Empty");
        isEmpty = true;
    }
    else if(h === ""){
        alert("Hours of use Cannot Be Empty");
        isEmpty = true;
    }
    return isEmpty;
}

// add Row
function addHtmlTableRow()
{
    // get the table by id
    // create a new row and cells
    // get value from input text
    // set the values into row cell's
    if(!checkEmptyInput()){
    var newRow = table.insertRow(table.length),
        cell1 = newRow.insertCell(0),
        cell2 = newRow.insertCell(1),
        cell3 = newRow.insertCell(2),
        cell4 = newRow.insertCell(3),
        cell5 = newRow.insertCell(4),

        d = document.getElementById("d").value,
        q = document.getElementById("q").value,
        p = document.getElementById("p").value,
        h = document.getElementById("h").value,
        T = `${q*p*h}Wh`;

    cell1.innerHTML = d;
    cell2.innerHTML = q;
    cell3.innerHTML = p;
    cell4.innerHTML = h;
    cell5.innerHTML = T;

    // call the function to set the event to the new row
    selectedRowToInput();
}
}

// display selected row data into input text
function selectedRowToInput()
{

    for(var i = 1; i < table.rows.length; i++)
    {
        table.rows[i].onclick = function()
        {
            // get the selected row index
            rIndex = this.rowIndex;
            document.getElementById("d").value = this.cells[0].innerHTML;
            document.getElementById("q").value = this.cells[1].innerHTML;
            document.getElementById("p").value = this.cells[2].innerHTML;
            document.getElementById("h").value = this.cells[3].innerHTML;
        };
    }
}
selectedRowToInput();

function editHtmlTbleSelectedRow()
{
    var d = document.getElementById("d").value,
        q = document.getElementById("q").value,
        p = document.getElementById("p").value,
        h = document.getElementById("h").value;
    if(!checkEmptyInput()){
    table.rows[rIndex].cells[0].innerHTML = d;
    table.rows[rIndex].cells[1].innerHTML = q;
    table.rows[rIndex].cells[2].innerHTML = p;
    table.rows[rIndex].cells[3].innerHTML = h;
    }
}

function removeSelectedRow()
{
    table.deleteRow(rIndex);
    // clear input text
    document.getElementById("d").value = "";
    document.getElementById("q").value = "";
    document.getElementById("p").value = "";
    document.getElementById("h").value = "";
}

function totalPowerConsumption() {
    total = 0
    for(let i = 1; i < table.rows.length; i++){
        for(let j = 4; j < 5; j++) {
            tot = parseInt(table.rows[i].cells[j].innerHTML);
            total += tot;
        }
    }
    let show = document.getElementById("total");
    show.innerHTML = `${total}Wh`;
    show.style.display = "block";

}
function reset() {
	let b = document.getElementById("theTable")
	while(b.hasChildNodes()) {
		b.removeChild(b.lastChild);
	}
	document.getElementById("total").innerHTML = "";
	total1 = 0;

}





