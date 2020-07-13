from machine import Pin
from time import sleep

LED = Pin(16,Pin.OUT)

while(True):
    LED.on()
    sleep(0.2)
    LED.off()
    sleep(0.2)
