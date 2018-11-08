#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

while True:
	GPIO.output(21,1)
	time.sleep(0.1)
	GPIO.output(21,0)
	time.sleep(0.1)
	GPIO.output(21,1)
	time.sleep(0.05)
	GPIO.output(21,0)
	time.sleep(0.01)
	GPIO.output(21,0)
	time.sleep(0.1)
	GPIO.output(21,0)
	time.sleep(0.01)
	GPIO.output(21,0)
	time.sleep(0.05)
	GPIO.output(21,0)
	time.sleep(0.05)
	GPIO.output(21,0)
	time.sleep(0.7)
	GPIO.output(21,0)
	time.sleep(0.75)
	GPIO.output(21,0)
	time.sleep(0.80)

