document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const urlInput = document.getElementById('url');
        if (urlInput.value.trim() === '') {
            alert('Please enter a website URL.');
            event.preventDefault();
        }
    });
});