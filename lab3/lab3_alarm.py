import machine
import ssd1306
import time
from machine import RTC, Pin, I2C, PWM

A = Pin(0, Pin.IN)
B = Pin(16, Pin.IN)  #pin16 does not have IRQ capabilities
C = Pin(2, Pin.IN)

i2c = I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
rtc = RTC()
datetime = rtc.datetime((2019, 10, 25, 0, 00, 02, 50, 0))  # the tuple is actually (year, month, day, weekday, hour, minute, second, millisecond).
alarmtime = [0, 0, 0]

cur1 = 0
cur2 = 0
pos1 = [6, 5, 4, 2, 1, 0]
pos2 = [2, 1, 0]


def blink():
    led = Pin(0, Pin.OUT)
    piezo = Pin(12, Pin.OUT)
    pwm = PWM(piezo)
    pwm.duty(3)
    led.value(0)
    time.sleep(5)
    led.value(1)
    pwm.duty(0)


def display_time():
    oled.fill(0)
    oled.text(("Time: %02d:%02d:%02d ") % (datetime[4], datetime[5], datetime[6]), 0, 0)
    oled.text(("Date: %d/%d/%d") % (datetime[0], datetime[1], datetime[2]), 0, 10)
    oled.text(("Clck: %02d:%02d:%02d ") % (alarmtime[0], alarmtime[1], alarmtime[2]), 0, 20)
    oled.show()

def change_pos(p):
    global cur1, cur2
    if B.value() == 1:
        cur1 = (cur1 + 1) % 6
    elif B.value() == 0:
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

    if datetime[4] == alarmtime[2] and datetime[5] == alarmtime[1] and datetime[6] == alarmtime[0]:
        blink()



