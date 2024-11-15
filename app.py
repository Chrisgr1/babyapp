# Using pygame for event-handling and sound
import pygame
import os
from collections import defaultdict

# Initialize pygame and the mixer
pygame.init()
pygame.mixer.init()

# Disable mouse functionality
pygame.mouse.set_visible(False)  # Hide the mouse cursor
pygame.event.set_blocked(pygame.MOUSEMOTION)  # Block mouse motion events
pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)  # Block mouse button down events
pygame.event.set_blocked(pygame.MOUSEBUTTONUP)  # Block mouse button up events

# Define the directory where the sound files are located
sound_dir = "/home/pi/apps/babyapp"

# Define the sound files for each section with absolute paths
sound_files = {
    'section1': os.path.join(sound_dir, 'BabySharkOrcaStra.mp3'),
    'section2': os.path.join(sound_dir, 'acousticguitar.mp3'),
    'section3': os.path.join(sound_dir, 'Carnival.mp3'),
    'section4': os.path.join(sound_dir, 'Fade to Black Metallica Harp Guitar Cover Jamie Dupuis.mp3'),
    'section5': os.path.join(sound_dir, 'Warsaw Guitar Orchestra The Call Of Ktulu.mp3'),
    'section6': os.path.join(sound_dir, 'Ali Bali Bee Hamish Imlach.mp3'),
    'section7': os.path.join(sound_dir, 'Ryu Theme Orchestral.mp3'),
    'section8': os.path.join(sound_dir, 'Glass Beams Mahal Live.mp3'),
}

# Define key mappings for each section
key_sections = {
    'section1': [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4],
    'section2': [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r],
    'section3': [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f],
    'section4': [pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v],
    'section5': [pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8],
    'section6': [pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o],
    'section7': [pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l],
    'section8': [pygame.K_n, pygame.K_m, pygame.K_COMMA, pygame.K_PERIOD],
}

# Initialize a dictionary to track key presses
key_press_counts = defaultdict(int)  # Default to 0 for any key

def play_sound(sound_file):
    """Plays a sound if no other sound is currently playing."""
    if pygame.mixer.music.get_busy():
        print(f"Music is currently playing. Ignoring: {sound_file}")
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
    """Main function to handle key press events and play corresponding sounds."""
    print("Press Ctrl + C to exit.")
    
    # Create a small window to capture events
    screen = pygame.display.set_mode((100, 100))
    running = True
    
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(f"Detected key: {event.key}")
                    
                    # Increment the key press count
                    key_press_counts[event.key] += 1

                    # Display the updated count
                    print(f"Key {pygame.key.name(event.key)} pressed {key_press_counts[event.key]} times.")
                    
                    # Check for Ctrl + C to exit
                    if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        print("Exiting...")
                        running = False
                    else:
                        # Check key mappings for each section
                        for section, keys in key_sections.items():
                            if event.key in keys:
                                play_sound(sound_files[section])
                                break
                elif event.type == pygame.QUIT:
                    running = False
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        # Print the final counts
        print("\nFinal Key Press Counts:")
        for key, count in key_press_counts.items():
            print(f"{pygame.key.name(key)}: {count}")
        pygame.quit()

if __name__ == "__main__":
    main()
