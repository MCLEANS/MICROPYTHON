
import machine
import time

def blink():
    pin = machine.Pin(16,machine.Pin.OUT)
    pin.off()
    time.sleep(1)
    pin.on()
    time.sleep(1)

    
    
blink()