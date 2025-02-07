document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".gong");
    const sounds = {};

    // Preload all audio files
    buttons.forEach(button => {
        const note = button.getAttribute("data-note");
        if (note) {
            sounds[note] = new Audio(`audio/${note}.mp3`); // Ensure MP3 files are inside the "audio/" folder
        }
    });

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const note = this.getAttribute("data-note");

            if (sounds[note]) {
                sounds[note].currentTime = 0; // Restart sound
                sounds[note].play().catch(error => console.log("Audio playback error:", error));
            } else {
                console.log(`Audio file not found: audio/${note}.mp3`);
            }
        });
    });
});
