#using pygame for event-handling and sound
import pygame
import os

# Initialize pygame
pygame.init()
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
    'section1': [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_BACKQUOTE],
    'section2': [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p],
    'section3': [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l],
    'section4': [pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n, pygame.K_m],
    'section5': [pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9, pygame.K_0, pygame.K_MINUS, pygame.K_EQUALS, pygame.K_LEFTBRACKET, pygame.K_RIGHTBRACKET, pygame.K_BACKSLASH],
    'section6': [pygame.K_SEMICOLON, pygame.K_QUOTE, pygame.K_COMMA, pygame.K_PERIOD, pygame.K_SLASH, pygame.K_BACKSLASH]
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
    screen = pygame.display.set_mode((100, 100))  # Create a small window to capture events
    running = True
    try:
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(f"Detected key: {event.key}")
                    if event.key == pygame.K_c and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        print("Exiting...")
                        running = False
                    else:
                        for section, keys in key_sections.items():
                            if event.key in keys:
                                play_sound(sound_files[section])
                                break
                elif event.type == pygame.QUIT:
                    running = False
    except KeyboardInterrupt:
        print("Program terminated by user.")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
