async function submitData() {
    const textInput = document.getElementById("textInput").value.trim();
    const fileInput = document.getElementById("fileInput").files[0];
    const responseDiv = document.getElementById("response");

    let formData = new FormData();

    if (textInput) {
        // If user entered text or URL, send it directly
        formData.append("input_data", textInput);
    } else if (fileInput) {
        // If user uploaded a file, send the file
        formData.append("file", fileInput);
    } else {
        responseDiv.innerHTML = "❌ Please enter CSV data, a URL, or upload a file.";
        return;
    }

    try {
        let response = await fetch("http://localhost:5000/process", {
            method: "POST",
            body: formData
        });

        // Check if the response is okay
        if (!response.ok) {
            throw new Error("HTTP error " + response.status);
        }

        // Parse JSON response
        let result = await response.json();

        // Display the response message
        if (result.message) {
            responseDiv.innerHTML = `✅ ${result.message}`;
            // Redirect to the chat interface after 2 seconds
            setTimeout(() => {
                window.location.href = "chat.html";
            }, 2000);
        } else if (result.error) {
            responseDiv.innerHTML = `❌ ${result.error}`;
        } else {
            responseDiv.innerHTML = "❌ Unexpected response format.";
        }
    } catch (error) {
        responseDiv.innerHTML = `❌ Error processing data: ${error.message}`;
    }
}
