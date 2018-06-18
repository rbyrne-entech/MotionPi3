from picamera import PiCamera
from time import sleep
import datetime
import RPi.GPIO as GPIO
from  httpRequest import formatJson
from httpRequest import postData
import sys
import base64
import logging

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin

#thresholdof motion detecton events for whether or not to take a picture
limit = 5
deviceId = "motionPi1"
sensorId = "motion1"



def take_a_pic(date_time):
    img="0"
    try:
        img = ('/home/pi/MotionPi3/MotionPi/images/%s.jpeg' % str(date_time))
	#camera.capture(img, resize(320,240))
	camera = PiCamera()
	camera.resolution = (640, 480)
	camera.framerate = (24, 1)

        camera.capture(img)
	
        camera.close()       
        
    except:
	logging.warning("Camera Close error")
	camera.close()
    finally:
        return img 

def detect_motion(date_time):
    while True:
        i = GPIO.input(11)
        if i == 0:                 #When output from motion sensor is LOW
        	date_time1 = datetime.datetime.now()	   
		print("No motion", date_time1, i)
            	sleep(.2)
        elif i == 1:               #When output from motion sensor is HIGH
            x=0
            while x<limit:
                  date_time1 = datetime.datetime.now()
		  print("Motion detected", date_time1, i)
                  if i==1:
                         x+=1
                  else:
                         break
                  if x==limit:
                         print("taking a pic")
                         pic = take_a_pic(date_time1)
                         while i ==1:
                                i = GPIO.input(11)
                                print("1")
                         return pic
                  i = GPIO.input(11)
                  #sleep(.2)
   
if __name__ == "__main__":
    while True:
        date_time = datetime.datetime.now()
	pic = detect_motion(date_time)
	if pic == "0":
		#log messge
		logging.warning("Bad pic")
	else:
            try:
		try:
                	with open(pic, 'rb') as f:
                   	     binPic = base64.b64encode(f.read())
#	    	    print(binPic)
                except:
			logging.warning("did not read picture")
			binpic="0"
		
	    	jsonData = formatJson(deviceId , sensorId, str(date_time), binPic)
		if jsonData == "0":
			logging.warning("json invalid")    
            	result = postData(jsonData) 
		
		if result == 200:
		         logging.info("Response: "+ str(result))
	 	else:
		         logging.warning("Response "+ str(result))
            except:
		logging.warning("error sending data main")
                pass 
        # log the error
        # If post data returns error save locally at somepoint

