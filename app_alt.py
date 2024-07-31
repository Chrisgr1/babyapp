import pygame
import keyboard
import os

# Initialize pygame mixer
pygame.mixer.init()

# Define the directory where the sound files are located
sound_dir = "/home/pi/apps/babyapp"

# Define the sound files for each section with absolute paths
sound_files = {
    'section1': os.path.join(sound_dir, 'Elefant.mp3'),
    'section2': os.path.join(sound_dir, 'cobra.mp3'),
    'section3': os.path.join(sound_dir, 'Kapuzineraffe.mp3'),
    'section4': os.path.join(sound_dir, 'geier.mp3'),
    'section5': os.path.join(sound_dir, 'Rhinozerus.mp3'),
    'section6': os.path.join(sound_dir, 'wolf.mp3'),
}

# Define key sections
key_sections = {
    'section1': ['1', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e', 'f', '`'],
    'section2': ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
    'section3': ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
    'section4': ['z', 'x', 'c', 'v', 'b', 'n', 'm'],
    'section5': ['6', '7', '8', '9', '0', '-', '=', '[', ']', '\\'],
    'section6': [';', "'", ',', '.', '/', '<', '>', '?']
}

def play_sound(key):
    if pygame.mixer.music.get_busy():
        return
    for section, keys in key_sections.items():
        if key in keys:
            sound_file = sound_files[section]
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            break

def main():
    print("Press Ctrl + C to exit.")
    try:
        while True:
            event = keyboard.read_event()
            if event.event_type == keyboard.KEY_DOWN:
                if event.name == 'c' and keyboard.is_pressed('ctrl'):
                    print("Exiting...")
                    break
                else:
                    play_sound(event.name)
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
