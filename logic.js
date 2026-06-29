const menuBtn = document.getElementById("menuBtn");
const dropdown = document.getElementById("dropdown");
const chatArea = document.getElementById("chatArea");
const msgInput = document.getElementById("msgInput");
const sendBtn = document.getElementById("sendBtn");

let isGenerating = false;

// ===========================
// Dropdown Menu
// ===========================

menuBtn.addEventListener("click", (e) => {

    e.stopPropagation();

    dropdown.classList.toggle("open");

});

document.addEventListener("click", () => {

    dropdown.classList.remove("open");

});

// ===========================
// Utility
// ===========================

function scrollToBottom() {

    chatArea.scrollTop = chatArea.scrollHeight;

}

// ===========================
// Chat Functions
// ===========================

function addMessage(text, sender) {

    const row = document.createElement("div");

    row.className = `msg-row ${sender}`;

    const bubble = document.createElement("div");

    bubble.className = "bubble";

    bubble.textContent = text;

    row.appendChild(bubble);

    chatArea.appendChild(row);

    scrollToBottom();

}

function createBotMessage() {

    const row = document.createElement("div");

    row.className = "msg-row bot";

    const bubble = document.createElement("div");

    bubble.className = "bubble";

    row.appendChild(bubble);

    chatArea.appendChild(row);

    scrollToBottom();

    return bubble;

}

// ===========================
// Send Message (Streaming)
// ===========================

async function handleSend() {

    if (isGenerating) return;

    const text = msgInput.value.trim();

    if (!text) return;

    isGenerating = true;

    addMessage(text, "user");

    msgInput.value = "";

    msgInput.disabled = true;

    sendBtn.disabled = true;

    const botBubble = createBotMessage();

    try {

        const response = await fetch("/chat", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                message: text

            })

        });

        if (!response.ok) {

            throw new Error("Server returned an error.");

        }

        const reader = response.body.getReader();

        const decoder = new TextDecoder();

        while (true) {

            const { done, value } = await reader.read();

            if (done) break;

            const chunk = decoder.decode(value, {

                stream: true

            });

            botBubble.textContent += chunk;

            scrollToBottom();

        }

    }

    catch (error) {

        console.error(error);

        botBubble.textContent =

            "⚠ Unable to contact M.A.L.D.I.N.I.";

    }

    finally {

        isGenerating = false;

        msgInput.disabled = false;

        sendBtn.disabled = false;

        msgInput.focus();

    }

}

// ===========================
// Event Listeners
// ===========================

sendBtn.addEventListener(

    "click",

    handleSend

);

msgInput.addEventListener("keydown", (event) => {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        handleSend();

    }

});