#!/usr/bin/env python

 
# import required libs
import time
import RPi.GPIO as GPIO

GPIO.cleanup() #cleaning up in case GPIOS have been preactivated
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# be sure you are setting pins accordingly
# GPIO17,GPIO18,GPIO22,GPI23
StepPins = [17,18,22,23]
 
# Set all pins as output
for pin in StepPins:
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)

#wait some time to start
time.sleep(0.5)
 
# Define some settings
StepCounter = 0
WaitTime = 0.0015
 
# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 1
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,1,1,1]
#Seq2[1] = [1,1,0,0]
#Seq2[2] = [0,1,0,0]
#Seq2[3] = [0,1,1,1]
#Seq2[4] = [0,0,1,0]
#Seq2[5] = [0,0,1,1]
#Seq2[6] = [0,0,0,1]
#Seq2[7] = [1,0,0,1]

 
# set
Seq = Seq2
StepCount = StepCount2

 
# Start main loop
try:
  while True:
    for pin in range(0, 4):
      xpin = StepPins[pin]
      if Seq[StepCounter][pin]!=0:
        print " Step %i Enable %i" %(StepCounter,xpin)
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)
    StepCounter += 1

  # If we reach the end of the sequence
  # start again
    if (StepCounter==StepCount):
      StepCounter = 0
    if (StepCounter<0):
      StepCounter = StepCount
 
  # Wait before moving on
    time.sleep(WaitTime)
except:
  GPIO.cleanup();
finally: #cleaning up and setting pins to low again (motors can get hot if you wont) 
  GPIO.cleanup();
  for pin in StepPins:
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin, False)
