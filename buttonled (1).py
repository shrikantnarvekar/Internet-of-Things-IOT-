#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)

GPIO.setup(21,GPIO.OUT)
GPIO.output(21,0)
try:
	while True:
		reading=GPIO.input(19)
		if reading ==0:
			print "Button pressed"
			GPIO.output(21,1)
			time.sleep(0.1)
		elif reading == 1:
			print "Button released"
			GPIO.output(21,0)
			time.sleep(0.1)
finally:
	GPIO.output(21,0)
	GPIO.cleanup()
			
