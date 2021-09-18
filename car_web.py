
  
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
#-----------------<setup>------------------
#setting variables for GPIO pins 17, 27, 10
led1 = 17
led2 = 27
led3 = 10

#set each led as an output:
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
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

#when no input have be passed it will render the html file so the web site will have an "look"
@app.route("/")
def main():
  return render_template('main.html')

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

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)

#you might have to swap the "+" pole and "-" pole or change a bit of the code, for the motors to work as it has been writen