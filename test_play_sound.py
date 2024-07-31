def test_play_sound():
    for sound_file in sound_files.values():
        if os.path.exists(sound_file):
            print(f"Testing sound: {sound_file}")
            try:
                pygame.mixer.music.load(sound_file)
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            except Exception as e:
                print(f"Failed to play sound: {e}")
        else:
            print(f"Sound file not found: {sound_file}")

if __name__ == "__main__":
    test_play_sound()
