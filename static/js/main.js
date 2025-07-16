// Dark mode toggle logic
function setDarkMode(on) {
    if (on) {
        document.body.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'on');
        document.getElementById('darkModeIcon').innerHTML = '<path d="M12 6a6 6 0 1 1-6 6c0-.265.015-.527.045-.785A6.978 6.978 0 0 0 12 6z"/>';
    } else {
        document.body.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'off');
        document.getElementById('darkModeIcon').innerHTML = '<path d="M6 0a7 7 0 0 0 0 14c3.866 0 7-3.134 7-7 0-.265-.015-.527-.045-.785A6.978 6.978 0 0 1 6 0z"/>';
    }
}
document.getElementById('darkModeToggle').addEventListener('click', function() {
    setDarkMode(!document.body.classList.contains('dark-mode'));
});
// On page load, set dark mode if previously chosen
if (localStorage.getItem('darkMode') === 'on') {
    document.body.classList.add('dark-mode');
    document.getElementById('darkModeIcon').innerHTML = '<path d="M12 6a6 6 0 1 1-6 6c0-.265.015-.527.045-.785A6.978 6.978 0 0 0 12 6z"/>';
} else {
    document.getElementById('darkModeIcon').innerHTML = '<path d="M6 0a7 7 0 0 0 0 14c3.866 0 7-3.134 7-7 0-.265-.015-.527-.045-.785A6.978 6.978 0 0 1 6 0z"/>';
} 