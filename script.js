document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".gong");

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const note = this.getAttribute("data-note");
            const audio = new Audio(`audio/${note}.mp3`); // Ensure MP3 files are in the "audio" folder
            
            audio.play().catch(error => console.log("Audio playback error:", error));
        });
    });
});