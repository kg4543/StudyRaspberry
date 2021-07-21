#Library
import time
import datetime as dt
from typing import OrderedDict
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import json

s2 = 23 # Raspberry pi PIN 23
s3 = 24 # Raspberry pi PIN 24
out = 25 # Raspberry pi PIN 25
NUM_CYCLES = 10

dev_id = 'MACHINE01'
broker_address = '210.119.12.92'
pub_topic = 'factory1/machine1/data/'

def send_data(param, red, green, blue):
    message = ''
    if(param == 'GREEN'):
        message = 'OK'
    elif(param == 'RED'):
        message = 'FAIL'
    elif(param == 'CONN'):
        message = 'CONNECTED'
    else:
        message = 'ERROR'

    currtime = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    #json data gen
    raw_data = OrderedDict()
    raw_data['DEV_ID'] = dev_id
    raw_data['PRC_TIME'] = currtime
    raw_data['PRC_MSG'] = message
    raw_data['COLOR'] = param
    raw_data['RED'] = red
    raw_data['GREEN'] = green
    raw_data['BLUE'] = blue
    
    pub_data = json.dumps(raw_data, ensure_ascii=False, indent='\t')
    print(pub_data)
    #mqtt_publish
    client2.publish(pub_topic, pub_data)

def read_value(a2, a3):
    GPIO.output(s2, a2)
    GPIO.output(s3, a3)
    # Set Time to set sensor
    time.sleep(0.3)
    # waiting
    #GPIO.wait_for_edge(out, GPIO.FALLING)
    #GPIO.wait_for_edge(out, GPIO.RISING)
    start = time.time() #current time
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(out, GPIO.FALLING)

    end = (time.time() - start)
    return NUM_CYCLES / end

def setup():
    ## GPIO setting
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(s2, GPIO.OUT)
    GPIO.setup(s3, GPIO.OUT)
    GPIO.setup(out, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    #get sensor result

def loop():
    result = ''

    while True:
        red = read_value(GPIO.LOW, GPIO.LOW) #s2 low, s3 low
        time.sleep(0.1) # Delay 0.1s
        green = read_value(GPIO.HIGH, GPIO.HIGH) #s2 high, s3 high
        time.sleep(0.1)
        blue = read_value(GPIO.LOW, GPIO.HIGH)

        print('red = {0}, green = {1}, blue={2})'.format(red, green, blue))
        if(red < 10): continue
        if(red > 2000 or green > 2000 or blue > 2000): continue
        
        if((red > green) and (red > blue)) :
            result = 'RED'
            send_data(result, red, green, blue)
        elif((green > red) and (green > blue)):
            result = 'GREEN'
            send_data(result, red, green, blue)
        else:
            result = 'ERROR'
        
        time.sleep(1)

#mqtt inti
print('MQTT Client')
client2 = mqtt.Client(dev_id)
client2.connect(broker_address)
print('MQTT Client connected')

if __name__ == '__main__':
    setup()    
    send_data('CONN', None, None, None) #sucees connection

    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()