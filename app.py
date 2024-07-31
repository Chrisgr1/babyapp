import pygame
import keyboard
import os

# Initialize pygame mixer
pygame.mixer.init()

# Define the directory where the sound files are located
sound_dir = "./"

# Define the sound files for each section with absolute paths
sounds = {
    'section1': pygame.mixer.Sound(os.path.join(sound_dir, 'Elefant.mp3')),
    'section2': pygame.mixer.Sound(os.path.join(sound_dir, 'cobra.mp3')),
    'section3': pygame.mixer.Sound(os.path.join(sound_dir, 'Kapuzineraffe.mp3')),
    'section4': pygame.mixer.Sound(os.path.join(sound_dir, 'geier.mp3')),
    'section5': pygame.mixer.Sound(os.path.join(sound_dir, 'Rhinozerus.mp3')),
    'section6': pygame.mixer.Sound(os.path.join(sound_dir, 'wolf.mp3')),
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
    # Stop any currently playing sounds
    for sound in sounds.values():
        if sound.get_num_channels() > 0:
            return

    for section, keys in key_sections.items():
        if key in keys:
            sounds[section].play()
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
