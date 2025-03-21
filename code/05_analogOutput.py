import board
from analogio import AnalogOut

analog_out = AnalogOut(board.A0)

while True:
    # Count up from 0 to 65535
    for i in range(0, 65536):
        analog_out.value = i