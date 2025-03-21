import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.A0)

def get_voltage(value):
    """
    Count up from 0 to 65535
    - 12 bit ADC however micropython
    scale to 16 bit
    """
    return (value * 3.3) / 65536

while True:
    analogIn = analog_in.value
    print(f"adc = {analogIn}")
    
    voltage = get_voltage(analogIn)
    print(f"volt = {voltage} V")
    
    time.sleep(0.1)