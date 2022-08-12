from flask import Flask, render_template, request, redirect
import threading
import socket
from gpiozero import MotionSensor
from gpiozero import LED
from time import sleep, time
from datetime import datetime

app = Flask(__name__)
pir = MotionSensor(pin=4,queue_len=5,sample_rate=120,threshold=0.2);
led = LED(17)
isOn = True
sleepTimeout = 5
host = socket.gethostbyname(socket.gethostname())

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/setTimer")
def setTimer():
    global isOn
    global sleepTimeout
    timeout = request.args.get('timeOut')
    sleepTimeout = int(timeout)
    isOn = False
    isOn = True
    return redirect('http://' + host + ':5000/', code=200)


@app.route("/changeState")
def changeState():
    global isOn
    reqState = request.args.get('state')
    if reqState == 'on':
        isOn = True
    else:
        isOn = False
    return redirect('http://' + host + ':5000/', code=200)

def threadedFunction():
    while isOn:
        if pir.motion_detected:
            led.on()
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print('Motion detected. Turned light on at: ', current_time)
            sleep(sleepTimeout)
        else:
            led.off()
            print('No motion found.')
            sleep(0.5)
        sleep(1)

threads = []
threadedLoop = threading.Thread(target=threadedFunction)
threads.append(threadedLoop)
threadedLoop.start()