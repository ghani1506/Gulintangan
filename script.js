document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".gong");
    const sounds = {};

    buttons.forEach(button => {
        const note = button.getAttribute("data-note");
        if (note) {
            sounds[note] = new Audio(`audio/${note}.mp3`);
            sounds[note].load(); // Preload audio to prevent delay
        }
    });

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const note = this.getAttribute("data-note");

            if (sounds[note]) {
                sounds[note].currentTime = 0;
                sounds[note].play().catch(error => console.log("Audio playback error:", error));
            } else {
                console.log(`Audio file not found: audio/${note}.mp3`);
            }
        });
    });
});
