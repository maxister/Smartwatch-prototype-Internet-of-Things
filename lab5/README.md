**Lab Five - Embedded Servers**

As the name implies, a server is a component or device that provides a service or function to a client device.
Any web page we can access through the Internet browser and applications, like games and video services, are hosted on servers
for users and clients to request and interact with. All a basic server does is take in requests from a client and sends back a
response.

In this lab, we make our smartwatch application (more specifically the ESP8266) into a server that will take requests
from a smartphone app through HTTP. More specifically, the smartphone APP sends commands or requests to the smartwatch 
server, and the smartwatch will execute these commands.

**Part One: Smartphone Application**

Create an Android smartphone application that will interface with the Google Speech API. 
The application should allow users to speak a voice command and send that command to the ESP8266 server via HTTP.
To download Android Studio, go to https://developer.android.com/studio/index.html and download the version appropriate for 
your operating system.

Once finish setting up the Android Studio, we can create an application that interfaces with the Google Speech API. 


**Part Two: Smartwatch Embedded Server**

1. Once the smartwatch application is done, we make sure the ESP8266 or smartwatch application can receive these requests. On the ESP8266 server, write a script that will allow the server to receive and process HTTP requests.

2. Configure the smartwatch display to turn off and turn on, display the time, and display any other message on the OLED 
whenever it receives the corresponding command from the smartphone. In other words, interface the smartphone app with the 
smartwatch embedded server. In order to access a server via HTTP on the Internet, 
the server must have a global IP address, which the ESP8266 does not have by default; it only has a local IP. 
To get around this, use ngrok to create a tunnel connection to the ESP8266.



