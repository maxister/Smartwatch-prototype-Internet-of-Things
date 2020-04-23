import network
import machine
import ssd1306
import socket
import time
from machine import Pin

i2c = machine.I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
rtc = machine.RTC()
rtc.datetime((2019, 10, 1, 0, 0, 0, 0, 0))

led = Pin(2, Pin.OUT)
led.value(1)
oled_on = False
trigger = False
display_time_now = False


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('Columbia University', '')
        while not sta_if.isconnected():
            pass
    return sta_if.ifconfig()


def display_time():
    oled.fill(0)
    cur_date = "date: " + str(rtc.datetime()[0]) + '/' + str(rtc.datetime()[1]) + '/' + str(rtc.datetime()[2])
    cur_time = "time: " + str(rtc.datetime()[4]) + ':' + str(rtc.datetime()[5]) + ':' + str(rtc.datetime()[6])
    oled.text(cur_date, 0, 0)
    oled.text(cur_time, 0, 10)
    oled.show()


ip_addr = do_connect()
#create socket-bind-listen
socket_addr = socket.getaddrinfo(ip_addr[0], 80)[0][-1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_INET:hostname+portnum
#Create a socket
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#Bind the socket to an address(IP+port num)
s.bind(socket_addr)
s.listen(1)
#Listen for connections with the listen() function
while True:
#Accept a connection with the accept() function system call
    cl, addr = s.accept()
    request = cl.recv(1024)
    request = str(request)

    if 'msg' in request:
        msg = request.split('/?msg=')[1].split('HTTP')[0]
        msg = msg.replace('%20', ' ')
        resp_msg = msg

        if 'morning' in msg:
            led.value(0)
            resp_msg = "light turn on"

        if 'night' in msg:
            led.value(1)
            resp_msg = "light turn off"

        if 'refresh' in msg:
            oled_on = True
            trigger = True
            resp_msg = "screen turn on"

        if 'stop' in msg:
            oled_on = False
            display_time_now = False
            resp_msg = "screen turn off"
            oled.fill(0)
            oled.show()

        if 'clock' in msg and oled_on:
            trigger = False
            resp_msg = "display time on the screen"
            display_time()

        if 'clock' in msg and not oled_on:
            display_time_now = False
            resp_msg = "please say 'refresh' to turn on the screen first"

        if oled_on and trigger:
            oled.fill(0)
            oled.text(msg, 0, 0)
            oled.show()
            resp_msg = msg

        suc_response = "HTTP/1.1 200 OK\r\n\r\n%s" % resp_msg
        cl.send(str.encode(suc_response))

    else:
        fail_response = "HTTP/1.1 501 Implemented\r\n\r\nPlease attach msg!"
        cl.send(str.encode(fail_response))

    cl.close()



