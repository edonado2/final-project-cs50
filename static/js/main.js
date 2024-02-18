async function searchMovies(query) {
    try {
        var apiKey = "50445d8592630acbc5c65378ad3843a7";
        var response = await fetch(`https://api.themoviedb.org/3/search/movie?api_key=${apiKey}&query=${encodeURIComponent(query)}&include_adult=false`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        var data = await response.json();
        displayResults(data.results);
        attachCardListeners();
    } catch (error) {
        console.error('Error:', error);
    }
}

function attachCardListeners() {
    const cards = document.querySelectorAll('.poster');
    cards.forEach(card => {
        const link = card.querySelector('a');
        if (link) {
            card.addEventListener('click', () => {
                const href = link.getAttribute('href');
                if (href) {
                    window.location.replace(href);
                }
            });
        }
    });
}
