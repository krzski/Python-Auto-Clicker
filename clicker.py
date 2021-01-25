import time
import sys
import subprocess

from pynput.mouse import Button, Controller
mouse = Controller()

from pynput.keyboard import Controller
keyboard = Controller()

# Installing required elements
subprocess.check_call([sys.executable,'-m', 'pip', 'install', 'pynput'])

# Set mouse coordinates (X, Y). If you want check coordinates use checkCoordinates.py
mouse.position = (900, 500)

# The number of repetitions of your click list
for clicks in range(2):
    # Waiting for next click in seconds
    time.sleep(1)

    # Number of clicks and mouse button
    mouse.click(Button.left, 1)

    # Print one letter, number and two chars with delay
    keyboard.press('A')
    keyboard.release('A')

    time.sleep(1)

    keyboard.press('1')
    keyboard.release('1')

    time.sleep(1)

    keyboard.press('@')
    keyboard.release('@')

    time.sleep(1)

    keyboard.press('@')
    keyboard.release('@')
