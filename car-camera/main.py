#project finnished 08-09-2021

from flask import Flask, render_template, Response
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
from camera_pi import Camera

app = Flask(__name__)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


"""   <setup>   """
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

@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')

"""   Code for the camera   """

def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

"""   Code for the motors   """

@app.route("/pin4/start")
def starting():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    return render_template("index.html")

@app.route("/pin4/off")
def offing():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    return render_template("index.html")

@app.route("/pin5/forward")
def forward():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    return render_template("index.html")
 
@app.route("/pin5/backward")
def backward():
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    return render_template("index.html")
 
@app.route("/pin6/low")
def low():
    p.ChangeDutyCycle(25)
    p2.ChangeDutyCycle(25)
    return render_template("index.html")
 
@app.route("/pin6/medium")
def medium():
    p.ChangeDutyCycle(50)
    p2.ChangeDutyCycle(50)
    return render_template("index.html")

@app.route("/pin6/high")
def high():
    p.ChangeDutyCycle(75)
    p2.ChangeDutyCycle(75)
    return render_template("index.html")

@app.route("/pin7/sl")
def sl():
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    return render_template("index.html")

@app.route("/pin7/sr")
def sr():
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    return render_template("index.html")

@app.route("/pin8/tl")
def tl():
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
    return render_template("index.html")

@app.route("/pin8/tr")
def tr():
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    GPIO.output(in1,GPIO.HIGH) 
    GPIO.output(in2,GPIO.LOW)
#waits x amount of seconds:
    time.sleep(1)
#stops the motors:
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
