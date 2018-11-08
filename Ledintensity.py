#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

led_pin=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

pwm_led=GPIO.PWM(led_pin,500) #freq=500 object is created
pwm_led.start(100)
while True:
	duty_s=raw_input('Enter the brightnes between 0 to 100')
	duty=int(duty_s)
	pwm_led.ChangeDutyCycle(duty)
	time.sleep(0.5)
