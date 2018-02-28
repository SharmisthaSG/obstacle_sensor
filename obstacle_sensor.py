# time is used to calculate the distance 
# since the ultrasonic sensors send input in form of
# 0 and 1 (1 if obstacle is nearby, 0 otherwise)
# GPIO is a library that is used to interact with pins on Raspberry Pi
import RPi.GPIO as GPIO
import time

# Set Board Parameters
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)

# define constants TRIG1, TRIG2, ECHO1, ECHO2 
# sets up pins for interacting with ultrasonic sensors
# TRIG1 and TRIG2 are output pins 
# ECHO1 and ECHO2 are input pins 
TRIG1 = 16
TRIG2 = 15
ECHO1 = 18
ECHO2 = 22
DISTANCE = 17150

# set up pins for ultrasonic sensors 
# TRIG1, ECHO1 for sensor 1
# TRIG2, ECHO2 for sensor 2
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)

# setup motors two on each side
# pins 5 and 7 for left motors 
# pin 5 is for left motor A, pin 7 for left motor B
# pin 11 is for right motor A, pin 13 for right motor B
# pins 11 and 13 for right motors
GPIO.setup(5,GPIO.OUT) 
GPIO.setup(7,GPIO.OUT) 
GPIO.setup(11,GPIO.OUT) 
GPIO.setup(13,GPIO.OUT) 

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
flag = 1

GPIO.setwarnings(False)

def distance(trig_value,ech_value):
    # the sensors send input as 1 if some obstacle is nearby and 0 otherwise
    # this function returns the distance 
    # based on time difference between the 0s and 1s sent by the sensors
    # parameters trig_value and each_value decide which sensor is to be used
    print("Measuring distance")
    GPIO.output(trig_value,False)
    print("Waiting")
    time.sleep(0.1)
    GPIO.output(trig_value,True)
    time.sleep(0.00001)
    GPIO.output(trig_value,False)
    
    # this loop updates the value of p_start till sensor sends 0
    while GPIO.input(ech_value)==0:
    	p_start = time.time()
    # this loop updates the value of p_end till sensor sends 1
    while GPIO.input(ech_value)==1:
    	p_end = time.time()

    p_duration = p_end-p_start
    dist = p_duration*DISTANCE 
    dist = round(dist,2)
    return dist

  
# this looks like the main haan main hi hai :p mann nahi tha main function banane ka. banaaaa <- wrap this in main
if __name__ == '__main__':
	while True:
    
	    while flag==1:
	      	# get distance of nearest obstacle from both sensors
	        d1 = distance(TRIG1,ECHO1)    
	        d2 = distance(TRIG2,ECHO2)
	        print(d1,d2)
          
          # we have an obstacle within 10 cm of sensor 1
  	      if d1<10.00 and d2>10.00:
	            print("obstacle near sensor 1")
  	          GPIO.output(5,1)
    	        GPIO.output(7,0)
      	      GPIO.output(11,1)
        	    GPIO.output(13,0)
          	  time.sleep(5)
            	GPIO.output(5,0)
	            GPIO.output(7,1)
	            GPIO.output(11,1)
	            GPIO.output(13,0)
	            time.sleep(5)
            
          # we have an obstacle within 10 cm of sensor 2
          if d2<10.00 and d1>10.00:
              print("obstacle near sensor 2")
              GPIO.output(5,1)
              GPIO.output(7,0)
              GPIO.output(11,1)
              GPIO.output(13,0)
              time.sleep(5)
              GPIO.output(5,1)
              GPIO.output(7,0)
              GPIO.output(11,0)
              GPIO.output(13,1)
              time.sleep(5)
              
          # we have an obstacle within 10 cm of sensor 1 and sensor 2
          if d1<10.00 and d2<10.00:
              print("obstacle at both sides")
              GPIO.output(5,1)
              GPIO.output(7,0)
              GPIO.output(11,1)
              GPIO.output(13,0)
              time.sleep(5)
              GPIO.output(5,1)
              GPIO.output(7,0)
              GPIO.output(11,0)
              GPIO.output(13,1)
              time.sleep(5)
              
          # we have no obstacle  
          if d1>10.00 and d2>10.00:
              print("no obstacle")
              GPIO.output(5,0)
              GPIO.output(7,1)
              GPIO.output(11,0)
              GPIO.output(13,1)
              time.sleep(5)

	# cleanup pins       
	GPIO.cleanup()
