#!/bin/bash
sudo apt update
sudo apt install -y ffmpeg libavdevice-dev libavfilter-dev libopus-dev
python3 -m pip install discord pillow
sudo apt install -y libjpeg-dev libfreetype6-dev
python3 -m pip install -U "discord.py[voice]"
echo "Dependencies installed successfully."
