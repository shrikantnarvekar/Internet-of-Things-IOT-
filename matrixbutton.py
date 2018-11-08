#!/usr/bin/env python
import os 
import max7219.led as led
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)#broadcom --value taken from bread board
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_UP)
matrix = led.matrix()	

def getCPUtemperature(reading):
	p=str(input("Enter your name:"))
	i=0
	J=1
	while True:
		reading1=GPIO.input(19)
		print(reading1)
		if(J==1 and reading1==1):
			device.show_message(p);
			i=i+2
		elif(i>1 and reading1==0):
			print("hello")
			J=2
			getCPUtemperature(reading)
device = led.matrix(2)
device.orientation(270)
try:
	while True:
		reading=GPIO.input(19)
		if(reading==0):
			getCPUtemperature(reading)
		elif(reading==1):
			print ("button preased")
			
except KeyboardInterrupt:
	pass
finally:
	device.clear()
