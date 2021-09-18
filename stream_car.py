#!/usr/bin/env python
#  	appCam.py

#Imports the modules
from flask import Flask, render_template, Response
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
from camera_pi import Camera
# Raspberry Pi camera module (requires picamera package)

#For the car and a bit web
app = Flask(__name__)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

"""car setup and varibles to car"""

#setup pins variable for left motor:
in1 = 24
in2 = 23
en = 25
temp1=1
#setup pins variable for right motor:
in3 = 16
in4 = 20
en2 = 21
temp2=1

#setup for left motor:
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
#setup for right motor:
GPIO.setmode(GPIO.BCM)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
#how fast the motor spins and starts:
p=GPIO.PWM(en,150)
p2=GPIO.PWM(en2,150)
p.start(25)
p2.start(25)

"""end of the car setup and varibles to car"""

"""for the camera on the website"""

"""idel"""

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

"""idel"""

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

"""end of the camera"""

"""for the funktion of the car"""
#The function below is executed when someone requests a URL with the pin numbe$:
@app.route("/<pin>/<action>")
def action(pin, action):
#------------------<leds>--------------------
  if pin == "pin1" and action == "on":
    GPIO.output(led1, GPIO.HIGH)

  if pin == "pin1" and action == "off":
    GPIO.output(led1, GPIO.LOW)

  if pin == "pin2" and action == "on":
    GPIO.output(led2, GPIO.HIGH)

  if pin == "pin2" and action == "off":
    GPIO.output(led2, GPIO.LOW)

  if pin == "pin3" and action == "on":
    GPIO.output(led3, GPIO.HIGH)

  if pin == "pin3" and action == "off":
    GPIO.output(led3, GPIO.LOW)
#------------------<motor>------------------
  if pin == "pin4" and action == "start":
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    print("forward both")

  if pin == "pin4" and action == "off":
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

  if pin == "pin5" and action == "forward":
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)

  if pin == "pin5" and action == "backward":
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)

#------------------<speed>--------------------
    
  if pin == "pin6" and action == "low":
      p.ChangeDutyCycle(25)
      p2.ChangeDutyCycle(25)

  if pin == "pin6" and action == "medium":
    p.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)

  if pin == "pin6" and action == "high":
    p.ChangeDutyCycle(75)
    p2.ChangeDutyCycle(75)

#------------------<stering>--------------------

  if pin == "pin7" and action == "sl":
#right motor forward:
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
#left motor backward:
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
#input for stering right:

  if pin == "pin7" and action == "sr":
#right motor backward:
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
#left motor forward:
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)

  if pin == "pin8" and action == "tl":
#right motor forward:
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
#left motor backward:
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
#waits x amount of seconds:
    time.sleep(1)
#stops the motors:
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

  if pin == "pin8" and action == "tr":
#right motor backward:
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
#left motor forward:
    GPIO.output(in1,GPIO.HIGH) 
    GPIO.output(in2,GPIO.LOW)
#waits x amount of seconds:
    time.sleep(1)
#stops the motors:
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

  return render_template('main.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)