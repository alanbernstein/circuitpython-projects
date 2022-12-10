# neopixel_pedal_demo.py
#
#         usb power source
#                       |
#                  |  [usb]   |
#                 -| Bat  USB |- neopixel power
#   common ground -| Gnd    0 |- switch input
#                 -| 4     ~1 |-
#                 -| 3      2 |- neopixel data output
#                 -| Rst   3V |-

## library imports
import board
import neopixel
import time
import adafruit_dotstar
from digitalio import DigitalInOut, Direction, Pull


## color definitions
# add any RGB (Red, Green, Blue) or RGBW (Red, Green, Blue, White) color definitions here
RED = (255, 0, 0)
ORANGE = (255, 128, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
MAGENTA = (255, 0, 255)
WHITE = (255, 255, 255)
BRIGHT_WHITE = (0, 0, 0, 255)
BRIGHTEST_WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0)

## color cycle
# add any color cycle here
# color_cycle = [WHITE, BRIGHT_WHITE, BRIGHTEST_WHITE, BLACK]
color_cycle = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]


change_delay_seconds = 0.1    # how long the light stays on one color when you hold the pedal down
debounce_delay_seconds = 0.01 # tuning parameter for debouncing the switch input


## setup troubleshooting on-board LED:
board_led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
board_led.brightness = 0.10
board_led.fill(WHITE)  # white at startup
time.sleep(0.25)
board_led.fill(RED)  # red while initializing
time.sleep(0.25)


## set up external neopixel light device
pixels = neopixel.NeoPixel(board.D2, 8, brightness=0.1, pixel_order=neopixel.GRBW) # 8x1 stick
# pixels = neopixel.NeoPixel(board.D2, 100, brightness=0.1, pixel_order=neopixel.GRB) # high density strip

color_index = 0
pixels.fill(color_cycle[color_index])


## set up pedal input
switch = DigitalInOut(board.D0)  # connect the pedal switch to pin 0
switch.direction = Direction.INPUT
switch.pull = Pull.UP


## run main loop
board_led.fill(GREEN)

while True: 
    if switch.value:
        board_led.fill(GREEN)
    else:
        board_led.fill(BLACK)
        color_index = (color_index + 1) % len(color_cycle)
        time.sleep(change_delay_seconds)
    pixels.fill(color_cycle[color_index])

    time.sleep(debounce_delay_seconds)
