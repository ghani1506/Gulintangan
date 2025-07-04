import pygame
import os
import sys

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Set up screen
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Caklempong Instrument")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BRASS = (181, 166, 66)
GREY = (100, 100, 100)

# Define notes and positions
lower_notes = ['C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3', 'C4']
upper_notes = ['C#3', 'D#3', '', 'F#3', 'G#3', 'A#3', '', '']

note_buttons = []

# Font
font = pygame.font.SysFont(None, 36)

def load_sound(note):
    path = os.path.join("sounds", f"{note}.WAV")
    if os.path.exists(path):
        return pygame.mixer.Sound(path)
    return None

# Create buttons for notes
button_width = 80
button_height = 80

for i, note in enumerate(lower_notes):
    rect = pygame.Rect(60 + i * (button_width + 10), 250, button_width, button_height)
    note_buttons.append((rect, note, load_sound(note)))

for i, note in enumerate(upper_notes):
    if note != '':
        rect = pygame.Rect(90 + i * (button_width + 10), 150, button_width - 30, button_height - 30)
        note_buttons.append((rect, note, load_sound(note)))

# Main loop
running = True
while running:
    screen.fill(WHITE)

    for rect, note, sound in note_buttons:
        # Draw buttons
        color = BRASS if len(note) == 2 else GREY
        pygame.draw.ellipse(screen, color, rect)
        pygame.draw.ellipse(screen, BLACK, rect, 2)

        # Draw note text
        text = font.render(note, True, BLACK)
        text_rect = text.get_rect(center=rect.center)
        screen.blit(text, text_rect)

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            for rect, note, sound in note_buttons:
                if rect.collidepoint(pos):
                    if sound:
                        sound.play()
                    else:
                        print(f"Sound for {note} not found!")

    pygame.display.flip()

pygame.quit()
sys.exit()
