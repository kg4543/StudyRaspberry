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

@app.route('/')
def home():
	return render_template("webpage.html")
	 # render_template를 통해 html파일load

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
			md.ChangeDutyCycle(duty)
			return home()
	else:
		return home()

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
		distance = round((rtTotime * (34000/2)),2)
		time.sleep(1)
		print(distance, "cm")

if(__name__ == "__main__"):
	app.run(host='0.0.0.0', port='8080')
