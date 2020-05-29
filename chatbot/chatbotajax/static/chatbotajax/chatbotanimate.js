chatbotOpen = false;

function animateChatbot() {
    let chatbotBox = document.getElementById("chatbot-container");
    if (chatbotOpen) {
        chatbotDown()
    } else {
        chatbotUp()
    }
}


function chatbotUp() {
    let chatbotBox = document.getElementById("chatbot-container");
    chatbotBox.classList.add("chatbotup-animation");
    chatbotBox.classList.remove("chatbotdown-animation");

    let cross = document.getElementById("chatbot-close");
    cross.classList.add("fadeInAnimate")
    cross.classList.remove("fadeOutAnimate")

    chatbotOpen = true;
}

function chatbotDown() {
    let chatbotBox = document.getElementById("chatbot-container");
    chatbotBox.classList.add("chatbotdown-animation");
    chatbotBox.classList.remove("chatbotup-animation");

    let cross = document.getElementById("chatbot-close");
    cross.classList.add("fadeOutAnimate")
    cross.classList.remove("fadeInAnimate")

    chatbotOpen = false;
}
