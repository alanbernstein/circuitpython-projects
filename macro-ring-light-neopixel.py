# macro-ring-light-neopixel.py
#
#         usb power source
#                       |
#                  |  [usb]   |
#                  | Bat  USB |- neopixel power
# neopixel ground -| Gnd    0 |
# neopixel data   -| 4     ~1 |
#                  | 3      2 |
#                  | Rst   3V |

import time
import board
import adafruit_dotstar
import neopixel

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.05

RING_SIZE = 24
pixels = neopixel.NeoPixel(board.A3, RING_SIZE, pixel_order=neopixel.GRBW, brightness=0.0)
# RGB, RGBW, GRB, GRBW

delay = 0.5

for p in range(RING_SIZE):
    pixels[p] = (0, 0, 0, 255)

