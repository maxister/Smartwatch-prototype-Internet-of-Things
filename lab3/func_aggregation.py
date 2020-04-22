import machine
import ssd1306
import time
from machine import RTC, Pin, I2C, PWM

A = Pin(0, Pin.IN)
B = Pin(16, Pin.IN)  #pin16 does not have IRQ capabilities
C = Pin(2, Pin.IN)

i2c = I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c) #pixel
rtc = RTC()
datetime = rtc.datetime((2019, 10, 25, 0, 00, 02, 50, 0))  # the tuple is actually (year, month, day, weekday, hour, minute, second, millisecond).
alarmtime = [0, 0, 0] #time(hour, minute, second)

cur1 = 0 # to shift the
cur2 = 0
pos1 = [6, 5, 4, 2, 1, 0] ) #date time (for button 1+2)
pos2 = [2, 1, 0]  #date time (for button 1+3)

adc = machine.ADC(0)


def blink(): #alarm clock working
    led = Pin(0, Pin.OUT)
    piezo = Pin(12, Pin.OUT)
    pwm = PWM(piezo)
    pwm.duty(3) #3: for louder sound
    led.value(0)
    time.sleep(5)
    led.value(1)
    pwm.duty(0) # off


def display_time():
    oled.fill(0) #clear the screen
    oled.text(("Time: %02d:%02d:%02d ") % (datetime[4], datetime[5], datetime[6]), 0, 0)
    oled.text(("Date: %d/%d/%d") % (datetime[0], datetime[1], datetime[2]), 0, 10)
    oled.text(("Clck: %02d:%02d:%02d ") % (alarmtime[0], alarmtime[1], alarmtime[2]), 0, 20)
    oled.show()

def change_pos(p):
    global cur1, cur2
    if B.value() == 1:
        cur1 = (cur1 + 1) % 6#change pos of time
    elif B.value() == 0:     #change pos of alarm
        cur2 = (cur2 + 1) % 3

def acc_time(p):
    global cur, rtc
    if B.value() == 1:
        cur_datetime = list(datetime)
        cur_datetime[pos1[cur1]] += 1
        rtc.datetime(tuple(cur_datetime))
    elif B.value() == 0:
        alarmtime[pos2[cur2]] += 1

A.irq(trigger = Pin.IRQ_FALLING, handler = change_pos)
C.irq(trigger = Pin.IRQ_FALLING, handler = acc_time)


while True:
    datetime = rtc.datetime()
    display_time()
    oled.contrast(adc.read())

    if datetime[4] == alarmtime[2] and datetime[5] == alarmtime[1] and datetime[6] == alarmtime[0]: #if the time is the same as alarm
        blink()



