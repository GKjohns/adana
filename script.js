const sendButton = document.getElementById("send-btn");
const chatWindow = document.querySelector(".chat-messages");
const adanaForm = document.getElementById("adana-form");

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

    // Bot essay
    const botEssay = document.createElement("div");
    botEssay.classList.add("bot");
    botEssay.innerHTML = `
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. In et leo at mi facilisis efficitur. Suspendisse non ultricies enim. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Integer auctor justo sit amet mi bibendum, eget fringilla dolor tempus. Etiam feugiat risus quam, ut auctor lorem tempor ac.</p>
        <p>Phasellus ultricies turpis nisl, eget pretium nunc bibendum eu. Aenean vestibulum diam eget quam tincidunt ullamcorper. Cras maximus purus vel quam vulputate, nec gravida massa pellentesque. Pellentesque egestas mi ac metus fringilla, eu fringilla arcu accumsan. Integer finibus, metus in fermentum eleifend, nisl urna pharetra sapien, vitae sollicitudin ligula urna vitae orci.</p>
        <p>Sed sit amet tincidunt justo. Suspendisse et sapien est. Cras ut urna vel justo cursus convallis eu in ipsum. Ut at vestibulum nunc. Aenean facilisis, felis ut rhoncus feugiat, quam mauris tempus orci, ut suscipit felis lectus sed purus. Sed venenatis risus vitae tortor commodo lacinia.</p>
    `;
    chatWindow.appendChild(botEssay);

    chatWindow.scrollTop = chatWindow.scrollHeight;
    adanaForm.reset();
});
