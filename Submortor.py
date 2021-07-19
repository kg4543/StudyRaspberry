#Library
import time
import datetime as dt
from typing import OrderedDict
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

def loop():
mortor = 21 # Raspberry pi PIN 21
## GPIO setting
GPIO.setmode(GPIO.BCM)
GPIO.setup(mortor, GPIO.OUT)
cycles = GPIO.PWM(mortor, 50)

while True:
	start = time.time()
	for i in range(10):
		cycles.start(0)
		cycles.ChangeDutyCycle(4)
		time.sleep(5)
		cycles.stop()
	WorkTime = time.time() - start
	print(WorkTime)

if(__name__ == '__main__'):
	try:
		loop()
	except KeyboardInterrupt:
		GPIO.cleanup()

