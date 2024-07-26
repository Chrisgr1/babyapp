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
