function send() {
    if (document.getElementById("chatbot-input").value === "") {
        return
    }
    let messageDiv = document.createElement("div");
    messageDiv.classList.add("chatbot-message");

    let message = document.createElement("p");
    message.classList.add("chatbot-sentmessage");

    let messageText = document.getElementById("chatbot-input").value;
    message.innerHTML = messageText;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            let messageDiv = document.createElement("div");
            messageDiv.classList.add("chatbot-message");
            let message = document.createElement("p");
            message.classList.add("chatbot-recvmessage");
            message.innerHTML = JSON.parse(xhttp.responseText)["reply"];
            messageDiv.appendChild(message);
            setTimeout(function() {
                document.getElementById("chatbot-message-container").appendChild(messageDiv);
                }, 2000)
        }
    }
    xhttp.open("POST", "/api/chatbot");
    xhttp.send(messageText);

    document.getElementById("chatbot-input").value = "";

    messageDiv.appendChild(message);

    document.getElementById("chatbot-message-container").appendChild(messageDiv);
}
