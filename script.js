document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".gong");
    const sounds = {};

    buttons.forEach(button => {
        const note = button.getAttribute("data-note");
        if (note) {
            sounds[note] = new Audio(`audio/${note}.mp3`);
            sounds[note].preload = "auto";
        }
    });

    buttons.forEach(button => {
        button.addEventListener("pointerdown", function (event) { // Using pointerdown for instant response
            event.preventDefault(); // Prevent default behavior to allow multitouch
            const note = this.getAttribute("data-note");

            if (sounds[note]) {
                sounds[note].pause(); // Stop previous sound instantly
                sounds[note].currentTime = 0;
                sounds[note].play().catch(error => console.log("Audio playback error:", error));
            } else {
                console.log(`Audio file not found: audio/${note}.mp3`);
            }
        }, { passive: false }); // Ensure event is not passive to allow multitouch
    });
});
