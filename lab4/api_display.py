import network
import urequests
import json
import machine
import ssd1306
from machine import Pin

i2c = machine.I2C(-1, Pin(5), Pin(4))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)


def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('Columbia University', '')  # sta_if.connect('<essid>', '<password>')
        while not sta_if.isconnected():
            pass


def main():
    do_connect()
    params = 0

    geo_url = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCGiis-vP7ZFXVbzifwdZtRnSNElfzPsKg'
    geo_inf = urequests.post(geo_url, data=json.dumps(params))
    geo_text = json.loads(geo_inf.text)

    lat = geo_text['location']['lat']
    lng = geo_text['location']['lng']

    weather_url = "http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=24b2e1ca7e2fd606243d8739744bd412" % (lat, lng)
    temp = json.loads(urequests.get(weather_url).text)['main']['temp'] - 273.15
    temp = round(temp, 1)
    temperature = str(temp)
    weather = json.loads(urequests.get(weather_url).text)['weather'][0]['main']

    while True:
        oled.fill(0)
        lat_text = 'lat: ' + str(lat)
        lng_text = 'lng: ' + str(lng)
        weather_temp = temperature +"C "+ weather

        oled.text(lat_text, 0, 0)
        oled.text(lng_text, 0, 10)
        oled.text(weather_temp, 0, 20)
        oled.show()


if __name__ == '__main__':
    main()
