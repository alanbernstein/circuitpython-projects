# auto_clicker.py
#
# WARNING: THIS PROGRAM MOVES THE MOUSE AND CLICKS THE
# LEFT BUTTON REPEATEDLY, WITH A SMALL INTERVAL. BE
# PREPARED TO DISABLE IT QUICKLY WHEN CONNECTING IT TO
# A LAPTOP OR PHONE.
#
# The purpose is to automatically click a phone screen,
# to grind through idle clicker games. This is for a
# specific game, on a specific phone model. It allows
# the player to progress through bonus stages and
# treasure chest hunts with no interaction, mostly just
# gathering collectibles in "active" mode automatically.
# It boosts, jumps, and fires arrows, all in a simple,
# repeated pattern.
#
# This was my third attempt at this program. The first
# was a proof on concept, it worked but was too simplistic.
# The second tried to do everything this one does, but
# failed because I misunderstood the way the HID mouse
# works.
#
# I recorded the positions of all the things I wanted to
# click from a phone screenshot, then copied them directly
# into a python list here. But the (x,y) input to the
# mouse.move function don't represent literal delta values.
# My assumption is that the host device interprets these
# numbers according to whatever speed/acceleration curve
# it wants, so thinking in terms of positions doesn't work.
#
# This version works by storing the correct deltas between
# each pair of positions in the sequence (`dxys`). These
# values were determined empirically, which was only a
# bit of a hassle, as the treasure chest delta-x is
# repeated so many times.

import math
import time
import board
import digitalio
from adafruit_hid.mouse import Mouse
import adafruit_dotstar


led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.04

select = digitalio.DigitalInOut(board.D0)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP

mouse = Mouse()


def go_to_corner(dx=1, dy=1):
    led[0] = (255, 255, 0)
    for n in range(22):
        mouse.move(x=dx*100)
    for n in range(22):
        mouse.move(y=dy*100)
    print('went to corner (%s, %s)' % (dx, dy))


CLICK = True

def long_press(t):
    if CLICK:
        mouse.press(Mouse.LEFT_BUTTON)
        time.sleep(t)
        mouse.release(Mouse.LEFT_BUTTON)

x1 = 140
y1 = 140

dxys = [
    [50, 80],    # boost
    [158, 290],  # chest 1 (top left)
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [0, -y1],  # chest 13 (middle right)
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    [-x1, 0],
    # add a boost here
    [240, -y1],  # chest 25 (bottom left)
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],
    [x1, 0],  # chest 30 (bottom right)
    [-160, -120],  # saver close / bonus start button
    [-160, -135],  # chest close button
    [-350, 0],     # boost
]

dt = 0.1

while True:
    print('x')
    go_to_corner(-1, 1)
    time.sleep(dt)
    for n in range(len(dxys)):
        mouse.move(x=dxys[n][0], y=-dxys[n][1])
        print(dxys[n])
        if n % 3 == 0:
            long_press(0.2)
            led[0] = (255, 0, 255)
        else:
            mouse.click(Mouse.LEFT_BUTTON)
            led[0] = (0, 255, 0)
        #elif n % 3 == 1:
        #    long_press(0.1)
        #    led[0] = (0, 255, 255)
        time.sleep(dt)
