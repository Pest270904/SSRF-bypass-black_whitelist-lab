async function generate(id) {
    const resultDiv = document.getElementById('result');
        resultDiv.textContent = 'Loading...';
        var apiUrl = "";

        switch(id) {
            case 'bw':
                apiUrl = `https://${window.location.hostname}/zeshiram`;
                break;
            case 'b':
                apiUrl = `https://${window.location.hostname}/zekrom`;
                break;
            case 'b_ez':
                apiUrl = `https://${window.location.hostname}/zekrom_easy`;
                break;
            case 'w':
                apiUrl = `https://${window.location.hostname}/reshiram`;
        }

        try {
            console.log(apiUrl);
            const response = await fetch(apiUrl, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ url: 'https://a-m7z4.onrender.com/' })
            });
            const data = await response.text();
            switch (id) {
                case 'bw':
                    resultDiv.textContent = `Random Number: ${data}   -   ` + (data % 2 == 0 ? 'Win':'Lose');
                    break;
                default:
                    resultDiv.textContent = `Random Number: ${data}   -   ` + (data > 50 ? 'Win':'Lose');
            }
        } catch (error) {
            resultDiv.textContent = 'Error fetching random number.';
        }
}

function showCode(file) {
    // Get references to the button and code container
    const toggleButton = document.getElementById('toggle-code-btn');
    const codeContainer = document.getElementById('code-container');

    if (codeContainer.style.display === 'none') {
        // Show the code
        codeContainer.style.display = 'block';
        toggleButton.textContent = 'Hide Code';
        toggleButton.classList.add('off');

        // Fetch and display the code
        fetch('/static/' + file) // Adjusted path for serving static file
            .then((response) => {
                if (response.ok) {
                    return response.text();
                } else {
                    throw new Error('Error: Could not load');
                }
            })
            .then((code) => {
                codeContainer.textContent = code;
            })
            .catch((error) => {
                codeContainer.textContent = error.message;
            });
    } else {
        // Hide the code
        codeContainer.style.display = 'none';
        toggleButton.textContent = 'Show Code';
        toggleButton.classList.remove('off');
    }
}