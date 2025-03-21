import time
import board
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.GP0)
led.direction = Direction.OUTPUT

while True:
    led.value = True
    print("ON")
    time.sleep(1)
    
    led.value = False
    print("OFF")
    time.sleep(1)
