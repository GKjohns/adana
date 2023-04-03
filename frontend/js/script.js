const yearElement = document.getElementById("year");
const currentYear = new Date().getFullYear();
yearElement.textContent = currentYear;

const sendButton = document.getElementById("send-btn");
const chatWindow = document.querySelector(".chat-messages");
const adanaForm = document.getElementById("adana-form");

async function sendRequest(prompt) {
    const url = 'http://0.0.0.0:8881/api/predict';
    const data = { prompt: prompt };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const result = await response.json();
            console.log(result.response);

            return result
        } else {
            console.error('Error:', response.status);
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

sendButton.addEventListener("click", (event) => {
    event.preventDefault();

    const userMessage = document.getElementById("user-input").value;

    if (userMessage.trim() === "") {
        return;
    }

    // User message
    const userBubble = document.createElement("div");
    userBubble.classList.add("user");
    userBubble.textContent = userMessage;
    chatWindow.appendChild(userBubble);
    userBubble.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'nearest'});

    data_to_server = userMessage;

    const botEssay = document.createElement("div");
    botEssay.classList.add("bot");
    sendRequest(data_to_server)
        .then((result) => {
            botEssay.innerHTML = `<p>${result['response'].replace('\n', '</p>\n\n<p>')}</p>`
        })
        .then(() =>  botEssay.userBubble.scrollIntoView({ behavior: 'smooth', block: 'start', inline: 'nearest'}));
    
    chatWindow.appendChild(botEssay);
    // botEssay.userBubble.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
});
