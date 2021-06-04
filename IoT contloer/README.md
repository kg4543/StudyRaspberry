# 0. GPIO set

- GPIO.setmode(GPIO.BCM) : 핀 번호를 GPIO모듈 번호로 사용 / (GPIO.BOARD) : 핀 번호를 보드번호를 참조
- GPIO.setup(Pin,GPIO.IN or OUT) : 핀 번호에서 전류를 보내는지 받는지 설정
- GPIO.PWM(Pin,Frequency) : 초당 펄스의 주파수를 유지한 채, 펄스의 길이를 변화시킴 (출력 조절)
- global i : 전역변수로 설정

## PYTHON
```
from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

ledPin = 21
moodPin = 20
pianoPin = 2
triggerPin = 4
echoPin = 3
Melody = [131, 147, 165, 174, 196, 220, 247, 262]

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(moodPin, GPIO.OUT)
GPIO.setup(pianoPin, GPIO.OUT)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

md = GPIO.PWM(moodPin, 255)
Buzz = GPIO.PWM(pianoPin, 440)

global i
i =1
```

# 1. HomePage

- 'Flask/template' 폴더에 있는 웹페이지를 불러옴
- @app.route('/') : 첫페이지 로드 시 화면을 띄움

```
@app.route('/')
def home():
    return render_template("webpage.html")
     # render_template를 통해 html파일load
```

# 2. LED Controler

- ON / OFF Button을 활용해 LED의 불을 키고 끔
- POST를 통해 value 값을 전달
- request.form['led']을 통해 값을 받음

<kbd>![LED](/Capture/LED%20Control.PNG "LED Control")</kbd>

## HTML
```
<div>
		<h1>LED Control</h1>
		<form action = '/led' method = 'post'>
			<Button type = 'submit' name = 'led' value = 'ON'>ON</Button>
			<Button type = 'submit' name = 'led' value = 'OFF'>OFF</Button>
			<Button type = 'submit' name = 'led' value = 'CLEAN'>CLEAN</Button>
		</form>
</div>
```
## PYTHON
```
@app.route('/led', methods = ['POST'])
def led():
    data = request.form['led']
    if(data == 'ON'):
        GPIO.output(ledPin, 1)
        return home()
    elif(data == 'OFF'):
        GPIO.output(ledPin, 0)
        return home()
    else:
        GPIO.cleanup()
        return home()
```

# 3. MOOD LED Controler

- webpage의 textbox에 값을 입력하여 그 값을 전달
- 전달 받은 값을 int로 형 변환하여 'duty'에 저장
- 사전에 설정한 PWM(md)를 통해 'duty' 값 만큼 출력을 조절 
- ex) duty = 50 -> 50% 출력
      PWM : 1sec에 5V를 출력해야할 경우 0.5sec만 5V를 출력 

<kbd>![MOOD](/Capture/Mood%20Control.PNG "MOOD Control")</kbd>

## HTML
```
<div>
		<h1>Mood Light Control</h1>
		<form action = '/mood' method = 'post'>
			<input type = 'text' name = 'mod' />
			<Button type = 'submit'>ON</Button>
		</form>
</div>
```
## PYTHON
```
@app.route('/mood', methods = ['POST'])
def mood():
    mod = request.form['mod']
    if(mod != ''):
        duty = int(mod)
        md.start(0)
        if(duty == 100):
            md.stop()
            return home()
    else:
        return home()
```

# 4. Speaker Controler

- textbox에서 1~8까지 수를 입력 데이터 전달
- 'ON' 값을 전달받아 if문 실행
- ChangeFrequency('Melody[]') : Melody배열을 불러와 전달받은 값을 통해 주파수 변경
- 이외의 값이 없거나 범위를 벗어날 경우 Home화면 출력
- 'OFF' 값을 전달받아 else문 실행

<kbd>![SPEAKER](/Capture/Speaker%20Control.PNG "Speaker Control")</kbd>

## HTML
```
<div>
		<h1>Speaker Control</h1>
		<form action = '/piano' method = 'post'>
			<input type = 'textbox' name = 'muz' />
			<Button type = 'submit' name = 'piano' value = 'ON'>ON</Button>
			<Button type = 'submit' name = 'piano' value = 'OFF'>OFF</Button>
		</form>
</div>
```
## PYTHON
```
@app.route('/piano', methods = ['POST'])
def piano():
    mus = request.form['muz']
    click = request.form['piano']
    if(click == 'ON'):
        if(mus != ''):
            muz = int(mus) - 1
            if(muz >= 0 and muz <= 7):
                Buzz.ChangeFrequency(Melody[muz])
                Buzz.start(50)
                return home()
            else:
                return home()
        else:
            return home()
    else:
        Buzz.stop()
        return home()
```

# 5. Ultra Sonic Controler

- 'ON' 값을 받을 시 전역함수 global i 를 1로 하여 while문을 실행
- 'OFF'일 경우 i를 0으로 하여 while문 종료
- 10u/s 주기로 TriggerPin에 (전파)출력을 하여 EchoPin에서 신호를 얼마나 받는지 시간을 측정
- 신호를 주고 받기까지의 시간을 거리로 계산 : 시간 * (34400/2)   
- 전파속력 344m/s, 편도 계산을 위해 2로 나눔 | 거리 = 속력 * 시간   

<kbd>![US](/Capture/UltraSonic%20Control.PNG "US Control")</kbd>

## HTML
```
<div>
		<h1>Ultra Sonic Control</h1>
		<form action = '/sonic' method = 'POST'>
			<Button type = 'submit' name = 'sonic' value = 'ON'>ON</Button>
			<Button type = 'submit' name = 'sonic' value = 'OFF'>OFF</Button>
		</form>
</div>
```
## PYTHON
```
@app.route('/sonic', methods = ['POST'])
def sonic():
    data = request.form['sonic']
    global i
    if (data == "ON"):
        i = 1
    if (data == "OFF"):
        i = 0
        return home()

    while i:
        GPIO.output(triggerPin,1)
        time.sleep(0.00001)
        GPIO.output(triggerPin,0)

        while GPIO.input(echoPin) == 0:
            start = time.time()
        while GPIO.input(echoPin) == 1:
            stop = time.time()

        rtTotime = stop - start
        distance = round((rtTotime * (34400/2)),2)
        time.sleep(1)
        print(distance, "cm")
```
