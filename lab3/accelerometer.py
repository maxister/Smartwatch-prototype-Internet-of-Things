import machine
import ssd1306
import time

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
spi = machine.SPI(1, baudrate=2000000, polarity=1, phase=1)
cs = machine.Pin(15, machine.Pin.OUT)


def get_pos():
    cs.value(0)
    pos_now=(spi.read(5,0xf3))#x2 = spi.read(5, 0xf3)
    cs.value(1)
    #cs.value(0)
    #y2 = spi.read(5, 0xf5)
    return [pos_now[1],pos_now[3]]
    #return [x2[1], y2[1]]


def main():
    # initialize the power of ADXL345
    power_ctl = b'\x2d\x08'   #0x2D: power control register;  D3: measure
    data_format = b'\x31\x0f'   #0x31 data format:D4
    cs.value(0)     #CS is the serial port enable line and is controlled by the SPI master.
    spi.write(power_ctl) #This line must go low at the start of a transmission and high at the end of a transmission
    cs.value(1)
    cs.value(0)
    spi.write(data_format)
    cs.value(1)

    # init position of the word in oled
    px, py = 50, 10
    while True:
        oled.fill(0)
        oled.text('Group8',px,py)
        oled.show()

        avg_x = get_pos()[0]
        avg_y = get_pos()[1]

        if 0 < avg_x < 128:
            px += avg_x
        if avg_x > 128:
            px -= 256 - avg_x

        if 0 < avg_y < 128:
            py -= avg_y/8
            #py -= avg_y

        if avg_y > 128:
            py += (256 - avg_y)/8
            #py += 256 - avg_y

        if px >= 128:
            px = 0
        if px < 0:
            px = 128
        if py >= 32:
            py = 0
        if py < 0:
            py = 32
        time.sleep(0.01)



        #time.sleep(0.001)


if __name__ == '__main__':
    main()