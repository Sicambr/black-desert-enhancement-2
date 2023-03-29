import ait
import time
from pynput.mouse import Button, Controller
import pynput


mouse = Controller()
# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

time.sleep(0.5)

# Set pointer position
mouse.position = (605, 467)
print('Now we have moved it to {0}'.format(
    mouse.position))

# Move pointer relative to current position
# mouse.move(500, -5)

# Press and release
# mouse.press(Button.left)
# mouse.release(Button.left)

# Double click; this is different from pressing and releasing
# twice on macOS
mouse.click(Button.left, 1)

# Scroll two steps down
# mouse.scroll(25, 0)
