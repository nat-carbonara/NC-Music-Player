import pygame
import mutagen
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from PIL import Image
import io
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk

# Setup Tkinter
root = tk.Tk()
root.title("NC Music Player 1.0 (30062025-1549")

# Selettore file
audio_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])

# Legge la copertina dal file MP3
audio = MP3(audio_path, ID3=ID3)

for tag in audio.tags.values():
    if isinstance(tag, APIC):
        image_data = tag.data
        img = Image.open(io.BytesIO(image_data))
        img = img.resize((300, 300))
        tk_img = ImageTk.PhotoImage(img)

        label = tk.Label(root, image=tk_img)
        label.pack()
        break

# Riproduzione audio
pygame.mixer.init()
pygame.mixer.music.load(audio_path)
pygame.mixer.music.play()

root.mainloop()
