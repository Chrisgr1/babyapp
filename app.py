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

# Define a single sound file for testing
test_sound_file = os.path.join(sound_dir, 'Elefant.mp3')

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
                        play_sound(test_sound_file)
    except KeyboardInterrupt:
        print("Program terminated by user.")

if __name__ == "__main__":
    main()
