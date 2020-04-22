**Lab Four - Interfacing with APIs**

An important concept behind many innovations and advancements is to build upon or improve what already exists. This not only saves our time because we can spend it elsewhere working on our own key contributions 
rather than reinventing something that has already been done, but it can also make our own products or innovations easier to use or interface with since they build upon existing technologies.
This is especially true for IoT systems and devices; one of the primary aims for IoT products is not only to allow for a 
network of communication between physical devices and systems, but to also do so in convenient manner by utilizing existing 
and flexible infrastructures.

In this lab, we will use Google APIs to add some nifty features to our smartwatch application.

An API (application programming interface) makes the primary functions and commands available to the user or developer, so that
they can utilize the existing technology or functionalities that the API provides. 
Just as a computer screen shows the user what is available or the functionalities on that computer,
an API shows the developer what features of the technology are available to use. While a user can communicate actions and 
commands to a computer through peripherals, like a mouse and keyboard, a developer can communicate with many APIs through HTTP,
an application layer communication protocol, or through the RESTful API, which uses HTTP as its basis.


For our smartwatch application, we will be using the Google Geolocation API and the OpenWeatherMap API to track the weather in our area and the Twitter API to send tweets with our smartwatch application. To incorporate these APIs, we must do the following on our ESP8266 embedded system.

**Part One: Geolocation and Weather**

1. Login to the Google API developer’s console at https://console.developers.google.com/. Enable the Geolocation API and       
create an API key to interface with the API through the ESP8266 through HTTP POST commands to the host address, 
https://www.googleapis.com, and by formatting your commands in JSON. This can be accomplished on the ESP8266 through the use 
of sockets. More information on how to setup the Google APIs are shown below.

After logging into the developers console, create a new project for our smartwatch and enable the API and set up the 
Google Geolocationing API on the developer’s console,


2. Display the coordinates received through Google Geolocationing API on the OLED display.
 
3. Feed the coordinates from the geolocation API into the OpenWeatherMap API to receive weather data for the location. 

Display the current weather (temperature and description (e.g. mostly cloudy)) on the OLED display.

**Part Two: Twitter**

Interface with the Twitter API to send tweets from ESP8266. 

