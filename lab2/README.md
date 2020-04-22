This lab aims to set up the ESP8266 board to read and process analog sensor data collected by sensors from the physical world and to generate a response from the board or other components based on our inputs.

The system is turned on when a user pushes a button, generating an interrupt, that is fed into one of the board’s GPIO pins. While the system is turned on the ADC will begin sampling from the sensor attached to the board’s only ADC pin. Based on the values read from the ADC, the system will turn on an LED and begin operating a piezo/vibration motor; the brightness of the LED and the pitch of the vibration motor will change based on the readings from the sensor and are controlled through PWM, a common method for controlling actuators. The sensor that we will be using in this lab is an analog light sensor.
Obtaining and processing sensor data is a vital part of IoT and human-machine interaction; every key pushed on your keyboard or button pressed on your mouse or phone is processed by your computer or laptop to produce an output on your device that people can control and use. The concepts and processes used in this lab will subsequently be incorporated into the final smartwatch to allow for human-machine interaction.

Part One: Reading in Sensor Data


The light sensor serves as the input, and LED and piezo serves as the output.

Hardware Setup:

We connect the analog light sensor to the ADC input to the HUZZAH board. In addition, We wire up an piezo and LED with an appropriate circuit to a GPIO pin on the ESP8266 and control the brightness of the LED with PWM.

Programming:
 We write a program to adjust the LED and piezo brightness and pitch based on our sensor input.

To be specific, we set the sampling frequency of light sensot to be 1 Hz (1 sample per second). 
The output would be an integer number. We vary the readings from the light sensor by placing our finger on the sensor and removing it to simulate the change of brightness in different environment.

We read the light sensor values at a rate of at least 10 Hz and based on the readings you get from the sensor, adjust the
pitch of the piezo/vibration motor and brightness of the LED accordingly (e.g. increase in light levels to an increase in LED brightness or piezo frequency).


Part Two: Interrupts and Debouncing

Hardware Setup:
We connect a button to the GPIO pins on the board to serve as an on-off switch. 

Programming:
We write a program to check the value of the GPIO pin connected to the button. The change of the value would raise the call of the interrupt function tha .

The interrupt function aims to check the value of the button and change the 'state' of the system. ie, if the button is pressed, the system will keep read values and adjust the output accordingly, while if the button is release, the system will enter sleep mode until the button is pressed again.
