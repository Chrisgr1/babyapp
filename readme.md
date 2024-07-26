Sure, here's the `README.md` file formatted in markdown:

```markdown
# Sound Keyboard for Babies

This is a simple Python program that plays sounds when specific keys are pressed. It divides the keyboard into six sections, each associated with a different sound. The program exits when `Ctrl + C` is pressed.

## Requirements

- Python 3
- `pygame`
- `keyboard`
- Additional libraries for MP3 support

## Installation

Follow these steps to set up and run the project:

### Step 1: Clone the Repository

1. Open your terminal.
2. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/yourusername/sound-keyboard.git
   cd sound-keyboard
   ```

### Step 2: Create and Activate a Virtual Environment

1. Create a virtual environment:
   ```bash
   python3 -m venv myenv
   ```
2. Activate the virtual environment:
   - On Unix or macOS:
     ```bash
     source myenv/bin/activate
     ```
   - On Windows:
     ```bash
     .\myenv\Scripts\activate
     ```

### Step 3: Create `requirements.txt`

Create a file named `requirements.txt` with the following content:
```plaintext
keyboard
```

### Step 4: Create `install_dependencies.sh`

Create a file named `install_dependencies.sh` with the following content:
```bash
#!/bin/bash

# Update package list
sudo apt-get update

# Install SDL2 mixer with MP3 support and other dependencies
sudo apt-get install -y libsdl2-mixer-2.0-0 libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
sudo apt-get install -y libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev

# Activate virtual environment and install Python dependencies
source myenv/bin/activate
pip install -r requirements.txt
pip install pygame
```

### Step 5: Make the Script Executable

1. Set the appropriate permissions for the `install_dependencies.sh` script:
   ```bash
   chmod +x install_dependencies.sh
   ```

### Step 6: Run the Dependency Installation Script

1. Execute the script to install all dependencies:
   ```bash
   ./install_dependencies.sh
   ```

### Step 7: Prepare Sound Files

1. Ensure you have the following MP3 files in the project directory:
   - Elefant.mp3
   - cobra.mp3
   - Kapuzineraffe.mp3
   - geier.mp3
   - Rhinozerus.mp3
   - wolf.mp3

### Step 8: Run the Program

1. With the virtual environment activated, run the program:
   ```bash
   python app.py
   ```

Press keys to hear sounds. Press `Ctrl + C` to exit the program.

## Usage

- `app.py`: Main program file
- `install_dependencies.sh`: Script to install necessary dependencies
- `requirements.txt`: List of Python dependencies

## Sounds

Place the following MP3 files in the project directory:
- Elefant.mp3
- cobra.mp3
- Kapuzineraffe.mp3
- geier.mp3
- Rhinozerus.mp3
- wolf.mp3
```
