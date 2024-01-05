
function submitForm(){
    let item_arr = document.getElementById("char_form").elements.namedItem("items").value;
    let relationship_arr = document.getElementById("char_form").elements.namedItem("relations").value;
	
    const xhr = new XMLHttpRequest();
    let form = document.forms[0];
	const port = 8000;
	const urlstring = "http://" + location.hostname + ":" + port + "/characters/updatechar";
    xhr.open(form.method, urlstring, true);
    let body = "{\"charId\" : {\"firstName\":" + "\"" + document.getElementById("char_form").elements.namedItem("first_name").value + "\"" +
		", \"lastName\":" + "\"" + document.getElementById("char_form").elements.namedItem("last_name").value + "\"" +
        ", \"curr_time\":" + document.getElementById("char_form").elements.namedItem("curr_time").value +
        "}, \"ability\":" + "\"" + document.getElementById("char_form").elements.namedItem("ability").value + "\"" +
        ", \"role\":" + "\""  + document.getElementById("char_form").elements.namedItem("role").value + "\"" +
        ", \"description\":" + "\""  + document.getElementById("char_form").elements.namedItem("description").value + "\"" +
        ", \"items\":" + "\""  + item_arr + "\"" +
        ", \"relations\":" + "\""  + relationship_arr + "\"" +  "}";
    xhr.setRequestHeader('Content-Type', 'application/json; charset UTF-8');
	
	var csrfToken = form.elements.namedItem("csrfmiddlewaretoken").value; //getCookie('csrftoken');
	xhr.setRequestHeader("X-CSRFToken", csrfToken);
	
    xhr.send(body);
}