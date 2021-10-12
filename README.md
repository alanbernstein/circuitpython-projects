Projects in CircuitPython on the [Trinket M0](https://www.adafruit.com/product/3500).


## How to use
Because CircuitPython works by running the `main.py` file on the chip, files in this repository have their filename repeated as the first line. This simplifies the process of figuring out what was running on a chip from an old/abandoned/temporary project.


## Boards

### Trinket M0
https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/pinouts


```
# |  [usb]   |
# | Bat  USB |
# | Gnd    0 |
# | 4     ~1 |
# | 3      2 |
# | Rst   3V |
```

Bat: voltage input, regulated down to 3V
USB: connected directly to USB port (which is what [usb] refers to)
3V: output from voltage regulator
GND: ground
Rst: reset
0: GPIO, analog input, PWM output, I2C (SDA)
1: GPIO, analog input, DAC output, capacitive touch
2: GPIO, analog input, PWM output, I2C (SCL), SPI (MISO)
3: GPIO, analog input, PWM output, SPI (SCK), UART (RX), capacitive touch
4: GPIO, analog input, PWM output, UART (TX), SPI (MOSI), capacitive touch


## Why
My introduction to microcontroller programming was with a freescale chip, in assembly, using [some program]. I enjoy the hobby, but that workflow was such a hassle, I never did anything else with that chip after finishing the class.

I later got into Arduino, using C, and the Arduino IDE. The improvement in the workflow was significant, but still left something to be desired.

Eventually I tried the trinket M0, huge improvement:
- "Burning" your program onto a chip is a *process*. With CircuitPython, all you need to do is save changes in your text editor.
- The program on the chip is editable.
- Works with any text editor and terminal program.
- Python is cleaner than C in terms of code clarity and conciseness, and dealing with dependencies. My projects are simple, there are no drawbacks to using python that affect to me.

Practically, these are great, because:
- The feedback cycle is much shorter.
- A microcontroller board can now contain brief documentation on what it contains!

Also, the trinket is tiny, it's small enough to be integrated into practically anything I could want to use it for. 5 pins is enough for a strip of lights and a few different input thingies.
