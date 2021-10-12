# zoom-macro-keyboard.py
#
#                cable to laptop
#                |
#           |  [usb]   |
#           | Bat  USB |- neopixel power
#           | Gnd    0 |
# switch A -| 4     ~1 |
# switch B -| 3      2 |- neopixel data
#           | Rst   3V |


import board
import digitalio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import time
import adafruit_dotstar
import neopixel


led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.010


button_pin_a = digitalio.DigitalInOut(board.A4)
button_pin_a.direction = digitalio.Direction.INPUT
button_pin_a.pull = digitalio.Pull.UP

button_pin_b = digitalio.DigitalInOut(board.A3)
button_pin_b.direction = digitalio.Direction.INPUT
button_pin_b.pull = digitalio.Pull.UP


kbd = Keyboard()

# aaaaaaaaaaaaaaaa

color_state_map = {False: (255, 0, 0), True: (0, 255, 0)}

debounce_delay = .050

last_debounce_time_a = 0
last_button_state_a = True
button_state_a = True
toggle_state_a = False  # state means "audio is active"

last_debounce_time_b = 0
last_button_state_b = True
button_state_b = True
toggle_state_b = False  # state means "video is active"

pixels = neopixel.NeoPixel(board.D2, 2)    # Feather wiring!
pixels[0] = (255, 0, 0)  # initial state is False, so show red
pixels[1] = (255, 0, 0)  # initial state is False, so show red


while True:
    reading_a = button_pin_a.value
    if reading_a != last_button_state_a:
        last_debounce_time_a = time.monotonic()

    if time.monotonic() - last_debounce_time_a > debounce_delay:
        if reading_a != button_state_a:
            button_state_a = reading_a
            if button_state_a == False:  # falling edge
                # shortcut to toggle zoom audio in macos
                # kbd.press(Keycode.SHIFT, Keycode.COMMAND, Keycode.A)
                kbd.press(Keycode.A)
                kbd.release_all()
                toggle_state_a = not toggle_state_a
                pixels[0] = color_state_map[toggle_state_a]

            # if button_state_a == True:  # rising edge

    reading_b = button_pin_b.value
    if reading_b != last_button_state_b:
        last_debounce_time_b = time.monotonic()

    if time.monotonic() - last_debounce_time_b > debounce_delay:
        if reading_b != button_state_b:
            button_state_b = reading_b

            if button_state_b == False:  # falling edge
                # shortcut to toggle zoom video in macos
                # kbd.press(Keycode.SHIFT, Keycode.COMMAND, Keycode.V)
                kbd.press(Keycode.B)
                kbd.release_all()
                toggle_state_b = not toggle_state_b
                pixels[1] = color_state_map[toggle_state_b]

            # if button_state_b == True:  # rising edge


    last_button_state_a = reading_a
    last_button_state_b = reading_b

