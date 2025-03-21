import time
import board
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.GP0)
led.direction = Direction.OUTPUT

switch = DigitalInOut(board.GP4)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if switch.value:
        led.value = False
        print("OFF")
    else:
        led.value = True
        print("ON")
        
    time.sleep(0.01)

