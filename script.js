document.querySelectorAll('.gong').forEach(button => {
    button.addEventListener('click', () => {
        const note = button.getAttribute('data-note');
        playSound(note);
    });
});

function playSound(note) {
    const audio = new Audio(`sounds/${note}.mp3`);
    audio.play();
}