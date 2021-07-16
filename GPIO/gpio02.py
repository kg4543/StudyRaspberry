import RPi.GPIO as GPIO
import time

red = 26
yellow = 19
green = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

if __name__ == '__main__':
    while True:
        GPIO.output(yellow, False)
        GPIO.output(red, True)
        time.sleep(3)
        GPIO.output(red, False)
        GPIO.output(green, True)
        time.sleep(5)
        GPIO.output(green, False)
        GPIO.output(yellow, True)
        time.sleep(1)
        