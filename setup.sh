#!/bin/bash
sudo apt update
sudo apt install -y ffmpeg libavdevice-dev libavfilter-dev libopus-dev
pip install discord pillow
sudo apt install -y libjpeg-dev libfreetype6-dev
git clone https://github.com/Rapptz/discord.py.git
cd discord.py
pip install -U .[voice]
cd ..
rm -rf discord.py

echo "Dependencies installed successfully."
