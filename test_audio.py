import pygame
import time
import os

pygame.mixer.init()
sound_dir = "/home/pi/apps/babyapp"
pygame.mixer.music.load(os.path.join(sound_dir, "Elefant.mp3"))
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)
