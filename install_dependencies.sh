#!/bin/bash

# Update package list
sudo apt-get update

# Install SDL2 mixer with MP3 support
sudo apt-get install -y libsdl2-mixer-2.0-0

# Install Python dependencies
pip install -r requirements.txt

