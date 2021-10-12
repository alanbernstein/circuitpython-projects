# neopixel_minimal.py
#         usb power source
#                       |
#                  |  [usb]   |
#                  | Bat  USB |- neopixel power
# neopixel ground -| Gnd    0 |
# neopixel data   -| 4     ~1 |
#                  | 3      2 |
#                  | Rst   3V |

import board
import neopixel

pixels = neopixel.NeoPixel(board.D4, 30)
pixels[0] = (255, 0, 0)
