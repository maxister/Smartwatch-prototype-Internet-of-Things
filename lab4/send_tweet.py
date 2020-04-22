import machine
import ssd1306
import urequests
import network
import time
from machine import Pin

i2c = machine.I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

msg_sent = False


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('Columbia University', '')
        while not sta_if.isconnected():
            pass

def send(p):
    global msg_sent
    msg_sent = True

def main():
    global msg_sent
    # press button_a to send a tweet
    button_a = Pin(0, Pin.IN, Pin.PULL_UP)
    button_a.irq(trigger=Pin.IRQ_FALLING, handler=send)

    do_connect()

    while True:
        oled.fill(0)
        oled.text("Press button A", 0, 0)
        oled.text("to send a tweet", 0, 10)
        oled.show()

        if msg_sent:
            msg = "This is IoT Lab4 Group8"
            url = "https://api.thingspeak.com/apps/thingtweet/1/statuses/update?api_key=%s&status=%s" % ("B9AH1P18CLNROFQY", msg)
            r = urequests.post(url)
            oled.fill(0)
            oled.text("Tweet sent", 0, 0)
            oled.show()
            time.sleep(10)
            msg_sent = False


if __name__ == '__main__':
    main()

