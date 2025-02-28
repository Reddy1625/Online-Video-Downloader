document.getElementById("downloadForm").addEventListener("submit", async function(event) {
    event.preventDefault();  // Prevent form from submitting the traditional way

    // Get the video link entered by the user from the form input
    const videoUrl = document.getElementById("videoUrl").value;

    // Check if the URL is provided
    if (!videoUrl) {
        document.getElementById("status").textContent = "Please enter a valid video URL.";
        return;
    }

    // Send POST request to FastAPI backend with the video URL in JSON format
    try {
        const response = await fetch('http://127.0.0.1:8000/download/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'  // Set content type to JSON
            },
            body: JSON.stringify({ link: videoUrl })  // Send URL as JSON in the request body
        });

        // Handle the response
        if (response.ok) {
            // If the response is successful, assume it's a file download
            const blob = await response.blob();
            const url = URL.createObjectURL(blob);

            // Create a download link dynamically
            const a = document.createElement("a");
            a.href = url;
            a.download = "downloaded_video.mp4"; // You can adjust the filename if needed
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);

            // Display the download message
            document.getElementById("status").textContent = "Download started! The video is being saved.";
        } else {
            // If response is not ok, show the error message
            const data = await response.json();
            document.getElementById("status").textContent = `Error: ${data.detail || "Something went wrong"}`;
        }

    } catch (error) {
        // Catch any error that happens during the fetch
        console.error("Error during video download:", error);
        document.getElementById("status").textContent = "There was an error with the request. Please try again.";
    }
});
