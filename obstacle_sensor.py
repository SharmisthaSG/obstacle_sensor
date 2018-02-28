import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD)
TRIG1=16
TRIG2=15
ECHO1=18
ECHO2=22
GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(ECHO2,GPIO.IN)

GPIO.setup(5,GPIO.OUT) #Left motor
#input A
GPIO.setup(7,GPIO.OUT) #Left motor
#input B
GPIO.setup(11,GPIO.OUT) #Right motor
#input A
GPIO.setup(13,GPIO.OUT) #Right motor
#input B

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
flag=1

GPIO.setwarnings(False)

def distance(trig_value,ech_value):
print("Measuring distance")
GPIO.output(trig_value,False)
print("Waiting")
time.sleep(0.1)#changed from 2 to 0.1
GPIO.output(trig_value,True)
time.sleep(0.00001)
GPIO.output(trig_value,False)
while GPIO.input(ech_value)==0:
p_start=time.time()
while GPIO.input(ech_value)==1:
p_end=time.time()
p_duration=p_end-p_start
dist=p_duration*17150
dist=round(dist,2)
return dist

while True:
    while flag==1:
#-now take input from ultrasonic sensor1
d1=distance(TRIG1,ECHO1)
d2=distance(TRIG2,ECHO2)
print(d1,d2)
#note--right now I am testing if two ultrasonic sensors work fine
#since the switch has not been connected yet, I have set the flag to 1
#COMPLETE--without switch as of date
if d1<10.00 and d2>10.00:
print("obstacle near sensor 1")
GPIO.output(5,1)
GPIO.output(7,0)
GPIO.output(11,1)
GPIO.output(13,0)
time.sleep(5)#change from 1 to 0.1
GPIO.output(5,0)
GPIO.output(7,1)
GPIO.output(11,1)
GPIO.output(13,0)
time.sleep(5)#change from 2 to 0.1
if d2<10.00 and d1>10.00:
print("obstacle near sensor 2")
GPIO.output(5,1)
GPIO.output(7,0)
GPIO.output(11,1)
GPIO.output(13,0)
time.sleep(5)#change from 1 to 0.1
GPIO.output(5,1)
GPIO.output(7,0)
GPIO.output(11,0)
GPIO.output(13,1)
time.sleep(5)#change from 1 to 0.1
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
if d1>10.00 and d2>10.00:
print("no obstacle")
GPIO.output(5,0)
GPIO.output(7,1)
GPIO.output(11,0)
GPIO.output(13,1)
time.sleep(5)
                '''print "Rotating both motors in clockwise direction"
                GPIO.output(5,1)
                GPIO.output(7,0)
                GPIO.output(11,1)
                GPIO.output(13,0)
                time.sleep(10) #One second delay
                print "Rotating both motors in anticlockwise direction"
    GPIO.output(5,0)
    GPIO.output(7,1)
    GPIO.output(11,0)
    GPIO.output(13,1)'''
    #time.sleep(10) #One second delay
GPIO.cleanup()

