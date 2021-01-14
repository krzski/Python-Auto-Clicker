import time
from pynput.mouse import Button, Controller
mouse = Controller()

# Set the time after which to check the cursor position
time.sleep(5)

print("Mouse coordinates: " + format(mouse.position))