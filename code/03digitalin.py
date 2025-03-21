import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP0)
led.direction = digitalio.Direction.OUTPUT

switch = digitalio.DigitalInOut(board.GP1)
switch.direction = digitalio.Direction.INPUT
switch.pull = Pull.UP

while True:
    if switch.value:
        led.value = False
    else:
        led.value = True
        
    time.sleep(0.01)
