import os
import sys
import tkinter as tk
from tkinter import messagebox
import threading
import sounddevice as sd
import soundfile as sf

# Screen setup
WIDTH, HEIGHT = 800, 400
root = tk.Tk()
root.title("Caklempong Instrument")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.configure(bg="white")

# Notes
lower_notes = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']
upper_notes = ['C#3', 'D#3', '', 'F#3', 'G#3', 'A#3', '', '']

# Load sound path
def load_sound(note):
    path = os.path.join("sounds", f"{note}.WAV")
    return path if os.path.exists(path) else None

# Play .WAV sound using sounddevice
def play_note(note_path):
    def _play():
        try:
            data, fs = sf.read(note_path, dtype='float32')
            sd.play(data, fs)
            sd.wait()
        except Exception as e:
            print(f"Error playing {note_path}: {e}")
    threading.Thread(target=_play).start()

# Create buttons
def create_buttons():
    for i, note in enumerate(lower_notes):
        path = load_sound(note)
        btn = tk.Button(
            root,
            text=note,
            bg="#B5A642" if path else "grey",
            fg="black",
            width=10,
            height=4,
            command=(lambda p=path, n=note: play_note(p) if p else messagebox.showwarning("Missing", f"Sound for {n} not found"))
        )
        btn.place(x=60 + i * 90, y=250)

    for i, note in enumerate(upper_notes):
        if note:
            path = load_sound(note)
            btn = tk.Button(
                root,
                text=note,
                bg="grey" if path else "lightgrey",
                fg="black",
                width=7,
                height=3,
                command=(lambda p=path, n=note: play_note(p) if p else messagebox.showwarning("Missing", f"Sound for {n} not found"))
            )
            btn.place(x=90 + i * 90, y=150)

# Build UI
create_buttons()

# Run main loop
root.mainloop()

