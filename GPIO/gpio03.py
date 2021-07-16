import RPi.GPIO as GPIO
import dht11
import time

pin = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

isnstance = dht11.DHT11(pin)

while True:
    try:
        result = isnstance.read()

        if result.is_valid():
            print('temp : {0}c / Humidity : {1}'.format(result.temperature, result.humidity))
        else:
            print('Read error : {0}'.format(result.error_code))
    except Exception:
        GPIO.cleanup()