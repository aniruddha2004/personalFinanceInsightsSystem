const chatHistory = document.getElementById("chatHistory");
const userQueryInput = document.getElementById("userQuery");

// Helper function to display messages in the chat
function addMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add(sender === "user" ? "user-message" : "bot-message");
    messageDiv.textContent = `${sender === "user" ? "You: " : "Assistant: "} ${message}`;
    chatHistory.appendChild(messageDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight; // Auto-scroll to the bottom
}

// Send user query to the backend
async function sendQuery() {
    const userQuery = userQueryInput.value.trim();
    if (!userQuery) {
        alert("Please enter a query.");
        return;
    }

    // Add the user's message to the chat
    addMessage("user", userQuery);

    try {
        const response = await fetch("http://localhost:5000/query", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ query: userQuery }),
        });

        const data = await response.json();

        // Add the bot's response to the chat
        if (data.message) {
            addMessage("bot", data.message);
        } else {
            addMessage("bot", "An error occurred while processing your query.");
        }
    } catch (error) {
        addMessage("bot", "Failed to connect to the server.");
        console.error(error);
    } finally {
        userQueryInput.value = ""; // Clear the input field
    }
}

// Allow pressing Enter to send the query
userQueryInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") {
        sendQuery();
    }
});
