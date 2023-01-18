#reciver side
import RPi.GPIO as GPIO
from time import sleep
from bluedot.btcomm import BluetoothClient
from signal import pause

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
set1=[19,21,23]#INPUT1,INPUT2,ENABLE OF LEFT MOTOR
set2=[11,13,15]#INPUT1,INPUT2,ENABLE OF RIGHT MOTOR

def forward():
    GPIO.output(set1[2],GPIO.HIGH)
    GPIO.output(set2[2],GPIO.HIGH)
    
    GPIO.output(set1[0],GPIO.HIGH)
    GPIO.output(set1[1],GPIO.LOW)
    
    GPIO.output(set2[0],GPIO.HIGH)
    GPIO.output(set2[1],GPIO.LOW)
    
    sleep(1)
    
    GPIO.output(set1[2],GPIO.LOW)
    GPIO.output(set2[2],GPIO.LOW)
    

def left():
    GPIO.output(set1[2],GPIO.HIGH)
    GPIO.output(set2[2],GPIO.HIGH)
    
    GPIO.output(set1[0],GPIO.HIGH)
    GPIO.output(set1[1],GPIO.LOW)
    
    GPIO.output(set2[0],GPIO.LOW)
    GPIO.output(set2[1],GPIO.HIGH)
    
    sleep(1)
    
    GPIO.output(set1[2],GPIO.LOW)
    GPIO.output(set2[2],GPIO.LOW)
    #move front
    forward()
    
    
 
def right():
    GPIO.output(set1[2],GPIO.HIGH)
    GPIO.output(set2[2],GPIO.HIGH)
    
    GPIO.output(set2[0],GPIO.HIGH)
    GPIO.output(set2[1],GPIO.LOW)
    
    GPIO.output(set1[0],GPIO.LOW)
    GPIO.output(set1[1],GPIO.HIGH)
    
    sleep(1)
    
    GPIO.output(set1[2],GPIO.LOW)
    GPIO.output(set2[2],GPIO.LOW)
    #move front
    forward()


for i in range(len(set1)):
    GPIO.setup(set1[i],GPIO.OUT)
    GPIO.setup(set2[i],GPIO.OUT)
    
#
#
#

def data_received(data):
    if data=="forward":
        forward()
        print("f")
    elif data == "left":
        left()
        print("l")
    elif data == "right":
        right()
        print("r")
sleep(7.5)
c = BluetoothClient("rncs", data_received)


pause()

GPIO.cleanup()
