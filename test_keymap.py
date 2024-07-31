import pygame
from inputs import get_key
import os

# Initialize pygame mixer with error handling
try:
    pygame.mixer.init()
    print("Pygame mixer initialized successfully.")
except Exception as e:
    print(f"Failed to initialize pygame mixer: {e}")

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
    'section1': ['KEY_1', 'KEY_2', 'KEY_3', 'KEY_4', 'KEY_5', 'KEY_A', 'KEY_B', 'KEY_C', 'KEY_D', 'KEY_E', 'KEY_F', 'KEY_GRAVE'],
    'section2': ['KEY_Q', 'KEY_W', 'KEY_E', 'KEY_R', 'KEY_T', 'KEY_Y', 'KEY_U', 'KEY_I', 'KEY_O', 'KEY_P'],
    'section3': ['KEY_A', 'KEY_S', 'KEY_D', 'KEY_F', 'KEY_G', 'KEY_H', 'KEY_J', 'KEY_K', 'KEY_L'],
    'section4': ['KEY_Z', 'KEY_X', 'KEY_C', 'KEY_V', 'KEY_B', 'KEY_N', 'KEY_M'],
    'section5': ['KEY_6', 'KEY_7', 'KEY_8', 'KEY_9', 'KEY_0', 'KEY_MINUS', 'KEY_EQUAL', 'KEY_LEFTBRACE', 'KEY_RIGHTBRACE', 'KEY_BACKSLASH'],
    'section6': ['KEY_SEMICOLON', 'KEY_APOSTROPHE', 'KEY_COMMA', 'KEY_DOT', 'KEY_SLASH', 'KEY_BACKSLASH']
}

def play_sound(sound_file):
    if pygame.mixer.music.get_busy():
        print(f"Music is currently playing, sound {sound_file} ignored.")
        return

    if os.path.exists(sound_file):
        print(f"Playing sound: {sound_file}")
        try:
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
        except Exception as e:
            print(f"Failed to play sound: {e}")
    else:
        print(f"Sound file not found: {sound_file}")

def main():
    print("Press Ctrl + C to exit.")
    try:
        while True:
            events = get_key()
            for event in events:
                if event.ev_type == 'Key':
                    key = event.ev_code
                    print(f"Detected key: {key}, state: {event.ev_state}")
                    if key == 'KEY_1' and event.ev_state == 1:
                        play_sound(sound_files['section1'])
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
