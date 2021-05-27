
var alertDiv = document.getElementById("alert-row");
var textArea = document.getElementById("user-input");



function submitUserInformation() {
    var userText = textArea.value.replace(/\s+/g, ' ').split(' ').filter((e) => e.length > 0);;
    console.log(userText);
    console.log("check")

    fetch('http://index/submit', {
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
        alertDiv.classList = "alert-row alert-success";
        alertDiv.innerHTML = '<h3>Sent Successfully</h3><br><p>${data}</p>'
    }).catch ( err => {
        alertDiv.innerHTML = "Error: ${err}"
    });
}




var submitBtn = document.getElementById("submit-this");
submitBtn.addEventListener("click", submitUserInformation);


