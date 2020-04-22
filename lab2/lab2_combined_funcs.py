import time
import machine
from machine import Pin, PWM, ADC

led = Pin(0, Pin.OUT)
piezo = Pin(12, Pin.OUT)

pwm1 = PWM(led)
pwm2 = PWM(piezo)

adc = machine.ADC(0)

def brightness(pwm1, a):
	pwm1.duty(a)

def pitch(pwm2, a):
    pwm2.duty(a)

button_edge = Pin(14, Pin.IN, Pin.PULL_UP)


def callback(p):
    while not button_edge.value():
    	a = int((1 - (adc.read() / 1024)) * 1023)
    	brightness(pwm1, a)
    	pitch(pwm2,a)
        time.sleep_ms(100)

button_edge.irq(trigger = Pin.IRQ_FALLING, handler = callback)

while True:
    brightness(pwm1, 1023)
    pitch(pwm2,1023)
    time.sleep_ms(100)



