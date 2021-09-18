# ***Python car***  

Det hära är en tutorial på hur man gör en bil med hjälp av en raspberry, en L298N motor driver och en pi kamera.

---

#### **Matrialet: för bygget:**

•	*Raspberry pi (1)*

•	*L298N motor driver (1)*

•	*12V DC motor (2)*

•	*9-12V Batteri (1)*

•	*Kablar*

#### **Paket installerade till raspberry pi** 

• *Flask*

• *Raspberry pi kamera*

---

## **Instruktioner för uppbygget till bilen (Hårdvara)**

#### **1. Koppla ihop raspberry till motor drivern (Höger sidan)**

* *GPIO 23 --> ENA (Vänster sidan)*

* *GPIO 25 --> IN1*

* *GPIO24 --> IN2*

#### **2. Koppla ihop raspberry till motor drivern (Vänster sidan av bilen)**

* *GPIO 16 --> IN3*

* *GPIO 20 --> IN4*

* *GPIO 21 -->	ENA (Höger sidan)*

#### **3. DC motor**

* *Vänster motor läg två kablar från de två poler till den blåa och skruva fast kablarna så att de sitter fast* 

* *Lika dant för höger motor som du gjorde för vänster.*

#### **4. 9-12V batteri**
* *Från batterins plus pol ska den till motor drivern 12V input `batteri --> 12V input`*

* *Från betterin minus pol ska till motor drivern ground. Du ska också har en ground kabel från raspberry pi till samma ground som motor drivern, exempel raspberry pi pin 3 --> motor drivern ground.*


![125340423-bf39ed00-e352-11eb-948f-4bf9b415d004](https://user-images.githubusercontent.com/87243876/132830465-d5dc4d06-8474-4aba-a597-217ef733b4ec.png)

---
## **Insallationer av Flask och pi kamera**

Installationen av `Flask` är rätt simpel. För att installera `Flask` är att gå in i terminalen och skriva in `pip install Flask` och testa efter ner laddningen med `flask --version`. 

För pi Kamera behöver man gå in i terminalen och skriva in `sudo raspi-config`, gå in till `interface Options` --> `Kamera` --> `yes`. För att testa kamerans funktionalitet kan man skriva in `raspistill -o Desktop/testphoto.jpg`. När du sätter in kameran på raspberry pi så stäng av den så inget går sönder.

*Om inte kameran skulle funka så kolla igen om kamera och enabled i inställningarna. Om den är enabled men inte fungerar så kan det vara andra paket i raspberry pi som hindrar Kameran att fungera, testa en annan raspberry pi.*


---

## **Instruktioner för koden till bilen**

Först så behöver man göra en mapp för bilen med `mkdir python_car` för att göra den första mappen som all kod sak innehålla. Efter det så ska vi göra två mappar till som ska innehålla HTML filen för hur websidan ska se ut och en till för CSS som designar websidan. För den första mappen ska den heta templates `mkdir templates` och den andra mappen ska heta static `mkdir static`. 

Det ska se ut så hära när du är klar:
```
└── python_car
    ├── templates
    │
    └── static
```

---
# **Färdiga koden**

* ### **index.html**

Gå in i templates mappen med `cd templates` och skapa ny fil med namnet `index.html` `sudo nano index.html`, nu bör du vara inne i .html filen, så kan du ta den färdiga koden här under och lägga in det i `index.html` filen. *Beskrivning av det grundläggande koden finns neders i documentet.*
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



Sen är vi klara med HTML filen och kan du gå ur filen med `ctrl + x` sen tryck på `J` och enter för att komma ut eller kan man trycka in `ctrl + s` och sedan in `ctrl + x` för två olika alternativ för att gå ur filen, och mappen med commando ``cd ..``

* ### **style.css**

Gå in i static mappen `cd static` och gör en ny fil som heter style.css `sudo nano style.css`, när du har kommit in i style filen kan du skriva in eller klistra in den hära koden:
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
Den hära koden ändrar hur bakrounden ändrar färg om du skulle byta ut exempel `background: blue` till `background: pink`, eller hur man vill align texten med ``text-align: center;``

Efter du har lagt till den coden så kan du spara filen och gå ut ur filen 

* ### **main.py**

Nu är det dags för att fixa python coden till datorn så att man kan styra och använda en websida med knappar och en kamera. (Fullständiga koden kommer att vara längst nere på documentet. )

Innan vi skapar filen så behöver du vara inne på `python car` mappen. Nu skapar vi en ny fil som heter `main.py` och gå in i den, och kan klistra in koden nedanför. *Beskrivning av det grundläggande koden finns neders i documentet.*

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

Nu borde allt vara installerat och nu borde allt fungera om du exekverar python koden med `python main.py` filen, om du fick ett error testa att lägga till sudo i början `sudo python main.html` så borde det fungera. 

* ### **camera.pi**

Nu kommer den sista filen för att cameran ska fungera med python koden. för att göra den så behöver du vara inne i `python_car` mappen och göra en ny fil med namnet `camera_pi.py`.

Klistra in denhära koden:
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



Det borde också se ut så hära i hela python_car directory
````markdown
└── python_car
    ├── main.py
    ├── camera_pi.py
    ├── templates
    │   └── index.html
    └── static
        └── style.css
````
Nu har du en fungerande websida med en kamera feed och fungerande knappar som styr bilen.

---
* ## **Beskrivning av koderna**

* ### **main.py**
Det hära är koden för all import moduler som man kommer att behöva använda. 
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
Den hära delen av koden är all installation och variablar för bilen. 
in1 har variablen 24 och när man kör `GPIO.setup` kan man se att då kommer variablen in1 så att koden vet att in1 har GPIO.OUT på BMC pin 24 på raspberry pi, och deta gör vi för alla pins som vi använder till bilenp `2=GPIO.PWM(en2,150)` och `p.start(25)` de bestämmer hur snabbt motorerna ska spina och starta.
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
Nästa del av koden är kamera funktionen till websidan.

Så den första `@app.route` så är det bara första en "render" som gör så att kan se all kod `index.html` så att det blir en hemsida att kolla på.
````python
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
````
Hära så är koden för att få video feeden från pi kameran så att i `index.html` filen kan rendra videon till websidan.
````python
"""   Code for the camera   """
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
````
Den näst sista delen av koden är hur man kommer att kunna styra motorerna med websidan.

I ´@app.route´ så kollar den vad som står i search box exempel `192.168.0.197` så kommer den bara att rendra `index.html` filen efter som i den första `@app.route('/')`. Men om man skulle trycka på en av knapparna, exempel knapp start så kommer search box att ändras från `192.168.0.197` till `192.168.0.197/pin4/start` då kommer den delen av koden att köras som i detta fall att motorerna startas och kör fram tills man trycker igen på stop eller någon annan knapp. och på slutet så returnar den en template som i detta fall är `index.html`

````python
@app.route("/pin4/start")
def starting():
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    return render_template("index.html")
````
Till sist så kommer den sista delen av koden som är tillför att få addresen till websidan och göra en port, sätta på debug och threaded. *Ibland så kan man behöva byta sin port om man har stänkt av pogramet och sutit på den ett antal gånger*
````python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port =80, debug=True, threaded=True)
````

* **index.html**

Nu kommer de grundläggade från HTML-filen

```html
  <head>
    <title>Live Streaming</title>
    <link rel="stylesheet" href='../static/style.css'/>
  </head>
```
Hära så kollar den på `style.css` filen inne i static mappen, för hur websidan ska se ut. 

```html
   <h3>
       <img src="{{ url_for('video_feed') }}" width="50%">
   </h3>
```
Hära så kommer man att få in video bilden till websidan med 50% av sin bredd.

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
Här skapar vi två styckna knappar som har chansen att ändra webadressen från exemel `xxx.xxx.xx.xxx/` till `xxx.xxx.xx.xxx/pin4/start`. Sen i python koden så kommer `@app.route` att se den har ändrats tilll `pin4/start` och kommer att sätta på motorerna för att gå framåt.

* **style.css**
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
Den hära koden ändrar hur bakrounden ändrar färg om du skulle byta ut exempel `background: blue` till `background: pink`, eller hur man vill align texten med ``text-align: center;``.

```css
  .left {
    float: left;
  }
```
`.left` i css koden letar efter `class` left i html koden så att man kan lägga det stycket till vänster, vilket i deta fall är video bilden på webbsidan.

````html
    <img class="left" src="{{ url_for('video_feed') }}" width="50%">
````

* **camera_pi**

Här kommer den del av koden som man kan ändra och fixa med.

```python
    def _thread(cls):
        with picamera.PiCamera() as camera:
            # camera setup
            camera.resolution = (320, 240)
            camera.hflip = True
            camera.vflip = True
```
Vid `camera.resolution` så kan man ändra kamerans resolution. 

Vid `camera.hfilp` och `camera.vflip` så kan man ändra hur kameran ska orgentera sig.`hflip` ändrar hur orgenteringen på videon är horizonelt och `vflip` ändrar hur den kommer att vara vertikalt. 