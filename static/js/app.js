
var reset = document.getElementById("reset");

var alertDiv = document.getElementById("alert-row");
var textArea = document.getElementById("user-input");


function submitUserInformation() {
    var userText = textArea.value.replace(/[^A-Za-z]+/g, ' ');
    console.log(userText);
    fetch('/api/submit', {
        method: 'POST',
        body:JSON.stringify({
            userInput: userText
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    }).then(response => {
        return response.text();
    }).then(data => {
        console.log(data)
        alertDiv.classList = "row-alert alert-success";
        alertDiv.innerHTML = `<h3 class="text-dark">Sent Successfully</h3><br><p class="text-dark">${data}</p>`
    }).catch ( err => {
        alertDiv.innerHTML = `Error: ${err}` 
    });
}

function clearText() {
    console.log("checking")
    textArea.value = ""
    alertDiv.innerHTML = ""
}
var submitBtn = document.getElementById("submit-this");
submitBtn.addEventListener("click", submitUserInformation)
reset.addEventListener("click", clearText)