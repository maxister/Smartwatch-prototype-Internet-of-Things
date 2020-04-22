
import time
import machine
from machine import Pin

led = Pin(0, Pin.OUT)

button_edge = Pin(14, Pin.IN, Pin.PULL_UP)

def callback(p):
    while not button_edge.value():
        led.value(0)
        time.sleep_ms(100)

button_edge.irq(trigger = Pin.IRQ_FALLING, handler = callback)

while True:
    led.value(1)
    time.sleep_ms(100)



