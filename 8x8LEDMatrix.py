#!/usr/bin/env python
import os 
import max7219.led as led

matrix = led.matrix()

def getCPUtemperature():
   res = os.popen("vcgencmd measure_temp").readline()
   return(res.replace("temp","").replace("'C\n",""))
	
device = led.matrix(2)
device.orientation(270)

try:
   while True:
      device.show_message("CPU Temperathure:"+getCPUtemperature()+"C");
except KeyboardInterrupt:
	pass
finally:
	device.clear()
		
	
