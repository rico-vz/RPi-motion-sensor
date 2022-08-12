# RPi Motion Sensor 💡🤖
 ![Py version](https://img.shields.io/badge/Python-3.9.2-yellow) ![Flask version](https://img.shields.io/badge/Flask-2.0.x-red)


I have integrated a LED Light, PIR Motion Sensor & a web page. When the PIR Motion Sensor detects motion the LED Light turns on for 5 seconds.

But if you want to keep the light on longer when it detects movement you can do this too!
We made a webpage with the help of [Flask](https://flask.palletsprojects.com/en/2.0.x/). 

![Website preview](https://i.imgur.com/qebbqFQ.png)
The input is in seconds, if you put 50 here then the LED will stay on for 50 seconds after motion is detected. 

## Requirements
To use this project you will need a few things:

 1. [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) 
 2. [PIR Motion Sensor](https://www.amazon.com/Adafruit-LK-918O-SANV-FBACA-PIR-Motion-Sensor/dp/B00JOZTAC6)
 3. [Basic Starter Kit](https://www.amazon.com/Smraza-Breadboard-Resistors-Mega2560-Raspberry/dp/B01HRR7EBG/ref=sr_1_3?keywords=Raspberry%20Pi%20LED&qid=1648043219&sr=8-3)
 4. Python & Flask installed on your RPi
 

 Having a slightly different motion sensor or starter kit shouldn't matter, worst-case you would need to slightly alter the code and settings of the Motion Sensor.

## Usage
Set up your Raspberry Pi with the PIR Motion Sensor & The LED.

Install [Flask](https://flask.palletsprojects.com/en/2.0.x/) on your Raspberry Pi.

Install gpiozero using pip

Clone this repository.

Go into the CLI on your Raspberry Pi (Using SSH or connect a M+KB on your R-Pi) and run:

    flask run --host=0.0.0.0

You can now visit the website at YOURIP:5000 and you'll be greeted with the control panel.

Enter a time (in seconds) and press Change.
The LED will now stay on for the duration specified. 

The time is updated as soon as you change it without any delay.
The loop to check for motion is ran in a seperate Thread and updates constantly.

Turning it fully on and off is also a breeze using our control panel.

Enjoy.
