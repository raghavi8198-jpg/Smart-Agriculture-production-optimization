document.getElementById("predictionForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    // Hide previous results
    const resultContainer = document.getElementById("resultContainer");
    const resultCard = document.getElementById("resultCard");
    const errorCard = document.getElementById("errorCard");

    resultContainer.classList.add("hidden");

    // Collect form data
    const data = {
        N: parseFloat(document.getElementById("N").value),
        P: parseFloat(document.getElementById("P").value),
        K: parseFloat(document.getElementById("K").value),
        temperature: parseFloat(document.getElementById("temperature").value),
        humidity: parseFloat(document.getElementById("humidity").value),
        ph: parseFloat(document.getElementById("ph").value),
        rainfall: parseFloat(document.getElementById("rainfall").value)
    };

    try {
        // Make API request
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.success) {
            // Show result card
            displaySuccess(result.crop, resultContainer, resultCard, errorCard);
        } else {
            // Show error card
            displayError(result.error, resultContainer, resultCard, errorCard);
        }
    } catch (error) {
        displayError("Network error. Please try again.", resultContainer, resultCard, errorCard);
    }
});

function displaySuccess(crop, resultContainer, resultCard, errorCard) {
    const cropName = document.getElementById("cropName");

    cropName.textContent = crop.charAt(0).toUpperCase() + crop.slice(1);

    errorCard.classList.add("hidden");
    resultCard.classList.remove("hidden");
    resultContainer.classList.remove("hidden");
}

function displayError(errorMsg, resultContainer, resultCard, errorCard) {
    const errorMessage = document.getElementById("errorMessage");

    errorMessage.textContent = errorMsg;

    resultCard.classList.add("hidden");
    errorCard.classList.remove("hidden");
    resultContainer.classList.remove("hidden");
}