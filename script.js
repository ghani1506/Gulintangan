document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".gong");

    buttons.forEach(button => {
        button.addEventListener("click", function () {
            const note = this.getAttribute("data-note");
            const audio = new Audio(`${note}.mp3`); // Remove "audio/" if files are in the same folder
            
            audio.play().catch(error => console.log("Audio playback error:", error));
        });
    });
});
