**Lab 3: Bus Communication - I2C and SPI**

A bus is an interface that allows different components to communicate with each other, so that each component can be 
modularized and focus on a single task or duty within the larger scope of the system. 
In this lab, we used two bus protocols that are common and popular in embedded and IoT systems: SPI and I2C. 
We use SPI to communicate with an accelerometer and I2C to communicate with an LCD screen and start building our smart watch.
To begin building our smartwatch application we must complete the following on our ESP8266.


**Part One: Displaying and Keeping Time**

Hardware setup:

Connect OLED to the ESP8266 (I2C pins). Light sensor is also connceted to ESP8266 to collect data from the environment, 
and the brightness of the OLED will change according to the environment brightness. 

Programming:

1. Obtain and modify the system time. When the ESP8266 boots up, its system time is reset to a default value; 
use the real-time clock (RTC) to set the system time.

2. Interface with the OLED screen through I2C and display the system time on the screen; the display should continuously 
update the time just like in a normal watch.

3. The OLED display shield comes with 3 buttons. We write programs in ways similar to Lab 2 to make use of interrupts
to adjust time according to the press and release of the button, and update the time displayed on the OLED.

4. Add in the functionality to read values from the light sensor andadjust the
display brightness or contrast depending on the brightness in the room.

**Part Two: Adding an Alarm**

Hardware Setup:

The same as Part 1

Programming:

1. Add in an alarm functionality, that allows you to set an alarm. When the system time reaches this time, the vibration motor/piezo should start vibrating to indicate that the alarm has gone off. Additionally, there should also be a visual indication.
2. Aim to combine the time and alarm functionalities into one system. In other words, combine parts one and two into one system.

**Part Three: Interfacing with the Accelerometer**

Hardware Setup:

Connect the accelerometer Connect OLED to the ESP8266 (SPI pins).

Programming:

1. Interface with the accelerometer and OLED screen using SPI.

2. Use the accelerometer readings and implement text scrolling. If the accelerometer is tilted far enough in one of the four
principal directions (up, down, left, right), the text on the screen should begin scrolling in the same direction. For
example, if the accelerometer the accelerometer is tilted to the right, the text on the screen scrolls to the right until 
it goes off screen before it reappears on the left side of the screen.

