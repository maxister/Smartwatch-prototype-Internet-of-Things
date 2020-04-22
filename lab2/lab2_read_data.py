import machine
import time
from machine import Pin, PWM, ADC

adc = machine.ADC(0)
led = Pin(0, Pin.OUT)
piezo = Pin(12, Pin.OUT)
pwm1 = PWM(led)
pwm2 = PWM(piezo)

def brightness(pwm1, a):
    # Value of duty cycle is between 0 and 1023 inclusive.
    pwm1.duty(a)

def pitch(pwm2, a):
    pwm2.duty(a)

m = 300

for i in range(m):
    a = int((1 - (adc.read() / 1024)) * 1023)
    brightness(pwm1, a)
    pitch(pwm2,a)
    time.sleep(0.05)

brightness(pwm1, 1023)
pitch(pwm2,1023)



