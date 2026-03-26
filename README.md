# Nikke Story Auto-Skip Script (PC)

For educational purposes only. Use responsibly and respect the game's Terms of Service.

This script automatically skips story dialogue in **Goddess of Victory: Nikke (PC)** using image recognition.

It detects the **Next** and **Skip** buttons on screen and presses the required keys automatically, reducing the need to manually click through dialogue.

## Requirements

Python 3.x

Install dependencies:

pip install pyautogui opencv-python numpy keyboard

## Setup

Place the following files in the same folder as the script:

nextstage.png
skip.png

These template images are required for button detection.

## Usage

Run:
python main.py

The script will continuously check the screen and skip dialogue when possible.
Close the terminal to stop the script.

## Notes

- Designed for **1920×1080 resolution**
- Other resolutions will likely require adjusting detection regions
- Uses OpenCV template matching on predefined screen regions to detect UI buttons.
