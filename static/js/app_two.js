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
        var clean_data = data.replace("\"","")
        var sets = clean_data.split(",")
        var all_sets = []
        sets.forEach(x=>{
            var temp = {}
            var first_set = x.split(" ")
            switch(first_set[0]){
                case "0":
                    temp.class = "Crime"
                    break
                case "1":
                    temp.class = "Entertainment"
                    break
                case "2":
                    temp.class = "Politics"
                    break
                case "3":
                    temp.class = "Science"
                    break
                default:
                    temp.class = "unknown"
            }
            temp.prob = first_set[1]
            all_sets.push(temp)
        })
        console.log(all_sets)
        all_sets.pop()
        
        alertDiv.classList = "row-alert alert-success";
        all_sets.forEach(x => {
            console.log(`${x.class}, ${x.prob}`);
            alertDiv.innerHTML += `<p class="text-dark"><b>Class:</b> ${x.class} <br /> <b>Prob:</b>  ${x.prob}</p>`
        })
      
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