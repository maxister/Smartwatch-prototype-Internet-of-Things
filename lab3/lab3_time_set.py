import machine
import ssd1306
import time
from machine import RTC, Pin, I2C

A = Pin(0, Pin.IN)
B = Pin(16, Pin.IN)
C = Pin(2, Pin.IN)

i2c = I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
rtc = RTC()
datetime = rtc.datetime((2019, 10, 25, 0, 23, 59, 50, 0))  # the tuple is actually (year, month, day, weekday, hour, minute, second, millisecond).

cur = 0
pos = [6, 5, 4, 2, 1, 0]


def display_time():
    oled.fill(0)
    oled.text(("%02d:%02d:%02d ") % (datetime[4], datetime[5], datetime[6]), 0, 0)
    oled.text("%d/%d/%d" % (datetime[0], datetime[1], datetime[2]), 0, 10)
    oled.show()

def change_pos(p):
    global cur
    cur = (cur + 1) % 6

def acc_time(p):
    global cur, rtc
    cur_datetime = list(datetime)
    cur_datetime[pos[cur]] += 1
    rtc.datetime(tuple(cur_datetime))

A.irq(trigger = Pin.IRQ_FALLING, handler = change_pos)
C.irq(trigger = Pin.IRQ_FALLING, handler = acc_time)

while True:
    datetime = rtc.datetime()
    display_time()
