const jokeBox = document.getElementById("jokeBox");

// Function to fetch a random joke
function fetchJoke() {
    // Show loading message
    jokeBox.querySelector("p").textContent = "Loading joke...";

    // Fetch random joke from the Official Joke API
    fetch("https://official-joke-api.appspot.com/random_joke")
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            // Display joke setup and punchline
            jokeBox.querySelector("p").innerHTML = `<strong>${data.setup}</strong><br>${data.punchline}`;
        })
        .catch(error => {
            jokeBox.querySelector("p").textContent = `Failed to load joke: ${error.message}`;
        });
}
