# 1. LED Controler

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

# 2. MOOD LED Controler

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

# 3. Speaker Controler

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

# 4. Ultra Sonic Controler

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
        distance = round((rtTotime * (34000/2)),2)
        time.sleep(1)
        print(distance, "cm")
```