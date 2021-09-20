# ***Python car***  

This is a tutorial about how to turn a raspberry pi into a working car with a raspberry pi camera.

---

#### **Material:**

•	*Raspberry pi (1)*

•	*raspberry pi camera*

•	*L298N motor driver (1)*

•	*12V DC motor (2)*

•	*9-12V Batteri (1)*

•	*Kablar*

#### **Raspberry pi software stuff:** 

• *Flask*

• *Raspberry pi camera*

---

## **car diagram**

#### **1. Right side of the car**

* *GPIO 23 --> ENA (Left side)*

* *GPIO 25 --> IN1*

* *GPIO24 --> IN2*

#### **2. Left side of the car**

* *GPIO 16 --> IN3*

* *GPIO 20 --> IN4*

* *GPIO 21 -->	ENA (Right side)*

#### **4. 9-12V battery**

* *From the battery plus side should go to the motor drivern 12V input `battery --> 12V input`* 

* *From the battery grund should to to motor drivern ground, and you should allso have a ground cable from the ground on the motor driver to the raspberry pi ground `raspberry pi pin 3 --> motor drivern ground`.* 

![125340423-bf39ed00-e352-11eb-948f-4bf9b415d004](https://user-images.githubusercontent.com/87243876/132830465-d5dc4d06-8474-4aba-a597-217ef733b4ec.png)

---
## **installation of Flask and raspberry pi camera**

The installation for `Flask` is feirly simpel. To install `Flask` you have to go in the terminal and type in `pip install Flask` and then test if the pakage has been downloadend with the command `flask --version`. 

For the pi camera you will have to go in the terminal och type in `sudo raspi-config` and then go to `interface Options` --> `camera` --> `yes`. For thesting if the pi camera is working test the comand `raspistill -o Desktop/testphoto.jpg` and see is a `test.jpg` has been created in the `Desktop` directory. When you put in the pi camera in to the raspberry pi you will have to turn off the pi so you don't burn the camera component or connector.

*If the camera would not work then test again if you have enabled the camera in the settings, or test another pi or new operativ system if you had installed other camera code*

---

## **Instruktions for the code**

First you will have to make the folder for all of the code with `mkdir python_car`. After this you will have to make two other folder for the HTML file and the CSS file, with the name templates `mkdir templates` and the other folder with the name static `mkdir static`.

It should be like this:
```
└── python_car
    ├── templates
    │
    └── static
```

---
# **Finished code**

* ### **index.html**

Now go in to the templates folder `cd templates` and create a new file `sudo nano index.html`, Now you should be in the index file and you can just copy the finished code in to the index file. **The basics of the code are at the bottom of the document**
````html
<!--
   index.html
-->

<html>

  <head>
    <title>Live Streaming</title>
    <link rel="stylesheet" href='../static/style.css' />
  </head>

  <body style="text-align: left;">
    <h1>Car Live Streaming</h1>
    <h3>
      <img class="left" src="{{ url_for('video_feed') }}" width="50%">
    </h3>

    <span class="right" style="float: right;">
      <h1 align="Right" ; style="color: goldenrod;">Motorer</h1>
      <h2 align="Right" ; style="color: black"> start and off
        <button>
          <a href="/pin4/start" style="color:black"> start</a>
        </button>
        <button>
          <a href="/pin4/off" style="color:black"> off</a>
        </button>
      </h2>

      <h2 align="Right" ; style="color: black"> Power
        <button>
          <a href="/pin4/start" style="color:black"> low</a>
        </button>
        <button>
          <a href="/pin4/off" style="color:black"> medium</a>
        </button>
        <button>
          <a href="/pin4/start" style="color:black"> high</a>
        </button>
      </h2>

      <h2 align="Right" ; style="color: black"> Stering
        <button>
          <a href="/pin7/sl" style="color:black"> Left</a>
        </button>
        <button>
          <a href="/pin7/sr" style="color:black"> Right</a>
        </button>
      </h2>

      <h2 align="Right" ; style="color: black"> Stering 1 second
        <button>
          <a href="/pin7/sl" style="color:black"> Left</a>
        </button>
        <button>
          <a href="/pin7/sr" style="color:black"> Right</a>
        </button>
      </h2>
    </span>
    <footer>>
      <hr>
      <p> @2021 Developed by Rasmus</p>
      <p>links for refrences:</p>
      <p> https://github.com/EbenKouao/SmartCCTV-Camera</p>
      <p>https://github.com/Mjrovai/Video-Streaming-with-Flask</p>
      <p>https://github.com/The1lama/python-car-L298N-motor-driver-with-web-controller</p>
    </footer>
  </body>
</html>
````
After copyed the code you can save and exit the file adn to to the `python_car` folder.

* ### **style.css**

Now go in to the `static` folder `cd static` and make a new file with the name style.css `sudo nano style.css`, when you have done the new file you can copy the code below:
```CSS
body {
    background: blue;
    color: yellow;
    padding: 1%;
    text-align: center;
  }
  
  .right {
    float: right;
  }
  
  .left {
    float: left;
  }
  
  footer {
    float: left;
  }
  
```
This code just changes the style of the webside for example you could change the backgorund colour from `background: blue` to `background: pink` or how to align the buttons or the video stream.

After this you can save and go out of the file and to to `python_car` foldern.

* ### **main.py**

Now it is time for the python code so we can get every thing to work with the car and camera.

When you are in the python car foldern you can create the python file with `sudo nano main.py` and copy the code below.

````python
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
````

Now save and exit the file.

* ### **camera.pi**

Now comes the last file for the for the project and this file will make the camera work with the webside. For the file name should be `camera_pi.py`

And then copy the code below:
```python
import time
import io
import threading
import picamera


class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera

    def initialize(self):
        if Camera.thread is None:
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                time.sleep(0)

    def get_frame(self):
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    @classmethod
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True
            camera.vflip = True

            # let camera warm up
            camera.start_preview()
            time.sleep(2)

            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg',
                                                 use_video_port=True):
                # store frame
                stream.seek(0)
                cls.frame = stream.read()

                # reset stream for next frame
                stream.seek(0)
                stream.truncate()

                # if there hasn't been any clients asking for frames in
                # the last 10 seconds stop the thread
                if time.time() - cls.last_access > 10:
                    break
        cls.thread = None
```

When you have finished making all of the files it should look like this
````markdown
└── python_car
    ├── main.py
    ├── camera_pi.py
    ├── templates
    │   └── index.html
    └── static
        └── style.css
````

And now every thing would work with the car, the webside and the camera feed.

---
* ## **description of the files**

* ### **main.py**
This bit of code is just to import all the pakages.
````python
from flask import Flask, render_template, Response
from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
from camera_pi import Camera

app = Flask(__name__)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
````

This part of the code is all the installations and varibles for the car
in1 is has the varible 24 which leter in the setup varibles `GPIO.setup` it knows that in1 has the is the BCM pin on the raspberry pi 
````python
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
````
The next part is the html code.

So in the beging you will see `@app.route` it just checks the URL what it will stan and in this part of the `@app.route` it will just render the  `index.html` so you can see everything.
````python
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
````
This part renders the camera function so you can have the video feed on the webside.
````python
"""   Code for the camera   """
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
````
The next part of the code will show how to make the motors go forward for example. 

In the `@app.route` it look after what the URL has for adress `192.168.0.197`. If you would press one of the buttons the URL would change from `192.168.0.197` to `192.168.0.197/pin4/start` for example, then the `@app.route` see that it has changed and then starts the pyhton code that is below and lasty renders the `index.html` file again so you can change the comand to stop or something else.
````python
@app.route("/pin4/start")
def starting():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    return render_template("index.html")
````
Last part of the code is the webadress and the port, debug and threaded. *Sometimes you will have to change the port if you have turned off the program and turnd on a couple of times.*
````python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
````

* **index.html**

Now comes the basics for the HTML-file

This check the styling for the webside `style.css` like where the buttons should be and the video feed.
```html
  <head>
    <title>Live Streaming</title>
    <link rel="stylesheet" href='../static/style.css'/>
  </head>
```
This is the place for the video feed and it has 50% of its width.
```html
   <h3>
       <img src="{{ url_for('video_feed') }}" width="50%">
   </h3>
```
This is just an example of how to create two diffrent buttons and how it changes the URL from example `xxx.xxx.xx.xxx/` to `xxx.xxx.xx.xxx/pin4/start` to start the motors, and then in the python code the `@app.route` sees that it has changes and starts that part of the code.
```html
         <h2 align="Right"; style="color: black"> start and off
              <button>
                 <a href="/pin4/start" style="color:black"> start</a>
              </button>
              <button>
                 <a href="/pin4/off" style="color:black"> off</a>
              </button>
         </h2>
```

* **style.css**

This changes the colur of the background for example `background: blue` to `background: pink`, or if you want to chage th etext alignent on the webside.
```CSS
body {
    background: blue;
    color: yellow;
    padding: 1%;
    text-align: center;
  }
  
  .right {
    float: right;
  }
  
  .left {
    float: left;
  }
  
  footer {
    float: left;
  }
  
```
`.left` is lokking after a `class left` in the html code så it can put the class to the left of the webside.
```css
  .left {
    float: left;
  }
```

* **camera_pi**

This part of the code you can change the camera of the resolution or if you vant to filp the camera. `hflip` changes the horizontal filp, `vflip` changes the vertical flip so if you would have the camera upside down you can change the organtation for the camera feed, without physicaly moving the camera. 

For the `camera.resolution` you can chagne the resolution of the camera if you want to have a better image.
```python
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True
            camera.vflip = True
``` 
