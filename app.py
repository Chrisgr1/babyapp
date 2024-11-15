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
sound_dir = "/home/pi/apps/new/babyapp"

# Define the sound files for each section with absolute paths
sound_files = {
    'section1': os.path.join(sound_dir, 'BabySharkOrcaStra.mp3'),
    'section2': os.path.join(sound_dir, 'acousticguitar.mp3'),
    'section3': os.path.join(sound_dir, 'carnival.mp3'),
    'section4': os.path.join(sound_dir, 'fadeharp.mp3'),
    'section5': os.path.join(sound_dir, 'WarsawKtulu.mp3'),
    'section6': os.path.join(sound_dir, 'AliBaliBee.mp3'),
    'section7': os.path.join(sound_dir, 'RyuTheme.mp3'),
    'section8': os.path.join(sound_dir, 'GlassBeams.mp3'),
}

# Define key mappings for each section
key_sections = {
    'section1': [
        pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, 
        pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0
    ],
    'section2': [
        pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, 
        pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p
    ],
    'section3': [
        pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, 
        pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l
    ],
    'section4': [
        pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, 
        pygame.K_n, pygame.K_m, pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH
    ],
    'section5': [
        pygame.K_TAB, pygame.K_SPACE, pygame.K_BACKSPACE, pygame.K_RETURN, 
        pygame.K_ESCAPE, pygame.K_MINUS, pygame.K_EQUALS, pygame.K_LEFTBRACKET, 
        pygame.K_RIGHTBRACKET, pygame.K_BACKSLASH
    ],
    'section6': [
        pygame.K_LCTRL, pygame.K_RCTRL, pygame.K_LALT, pygame.K_RALT, 
        pygame.K_LSHIFT, pygame.K_RSHIFT, pygame.K_CAPSLOCK
    ],
    'section7': [
        pygame.K_F1, pygame.K_F2, pygame.K_F3, pygame.K_F4, pygame.K_F5, 
        pygame.K_F6, pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_F10, 
        pygame.K_F11, pygame.K_F12
    ],
    'section8': [
        pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, 
        pygame.K_HOME, pygame.K_END, pygame.K_PAGEUP, pygame.K_PAGEDOWN, 
        pygame.K_INSERT, pygame.K_DELETE
    ],
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
    screen = pygame.display.set_mode((5000, 10000))
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
