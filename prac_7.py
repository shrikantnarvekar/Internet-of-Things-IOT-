#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
led_pin=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
pwm_led=GPIO.PWM(led_pin,500) #freq=500 object is created
pwm_led.start(0)
while True:
	for i in range (0,100):
		#duty_s=raw_input("Enter brightness between 0 to 100")
		duty=int(i)
		pwm_led.ChangeDutyCycle(duty)
		time.sleep(0.05)
	for i in range (100,0):
		#duty_s=raw_input("Enter brightness between 0 to 100")
		duty=int(i)
		pwm_led.ChangeDutyCycle(duty)
		time.sleep(0.05)
	
