var reset = document.getElementById("resettwo");

var alertDiv = document.getElementById("alert-row");
var textArea = document.getElementById("user-input-two");


function submitUserInformation() {
    var userText = textArea.value.replace(/[^A-Za-z]+/g, ' ');
    console.log(userText);
    fetch('/api/lda', {
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
        console.log(typeof data)
       // var classification = data.replace(/[^A-Za-z]+/g, ' ');
        alertDiv.classList = "row-alert alert-success";
        alertDiv.innerHTML = `<p class="text-dark">${data}</p>`
    }).catch ( err => {
        alertDiv.innerHTML = `Error: ${err}` 
    });
}

function clearText() {
    console.log("checking")
    textArea.value = ""
    alertDiv.innerHTML = ""
}
var submitBtn = document.getElementById("submit-two");
submitBtn.addEventListener("click", submitUserInformation)
reset.addEventListener("click", clearText)