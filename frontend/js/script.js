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

    const dataset = document.getElementById("dataset").value;
    const objective = document.getElementById("objective").value;

    if (objective.trim() === "") {
        return;
    }

    const userMessage = `Dataset: ${dataset}, Objective: ${objective}`;

    // User message
    const userBubble = document.createElement("div");
    userBubble.classList.add("user");
    userBubble.textContent = userMessage;
    chatWindow.appendChild(userBubble);
    userBubble.scrollIntoView({ behavior: 'smooth', block: 'nearest' });

    // Bot essay
    data_to_server = {
        dataset: dataset,
        objective: objective
    }
    
    const botEssay = document.createElement("div");
    botEssay.classList.add("bot");
    sendRequest(objective)
        .then((result) => {
            botEssay.innerHTML = `<p>${result['response'].replace('\n', '</p>\n\n<p>')}</p>`
        })
    
    chatWindow.appendChild(botEssay);
    userBubble.scrollIntoView({ behavior: 'smooth', block: 'nearest' });


    chatWindow.scrollTop = chatWindow.scrollHeight;
    adanaForm.reset();
});
