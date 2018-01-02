# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 11:38:56 2017

@author: David Burton
"""
#importing all of teh groundwork 
import ssd1306 #necssary for OLED
import mlx90614 #necessary for temperature sensor
import time #necessary for servo
from machine import I2C, Pin, PWM #necessary for servo and OLED
#this is so that while running the program, I know which section of my program went wrong
print("All modules imported fine") 

#creating the objects
servo=PWM(Pin(2), freq=50) #object that interacts with General Input Output Pin(2) connected to servo motor
i2c=I2C(scl=Pin(4), sda=Pin(5),freq=100000) #object that connects the OLED and sensor in some way...
oled=ssd1306.SSD1306_I2C(128, 64, i2c) #onject for interacting with the OLED
sensor=mlx90614.MLX90614(i2c) #object for interacting with the temperature sensor
print("All objects setup fine")

#creating functions to use
def findmax(somelist): #function to find the max item in a list
    maxer=0
    for i in somelist:
        if i>maxer:
            maxer=i
    return maxer

def findmin(somelist): #function to find the min item in a list
    miner=1000
    for i in somelist:
        if i<miner:
            miner=i
    return miner

def printit(a_list): #preparing stuff to print on OLED
    horizontal_pos=0 #starting the position for mapping
    maxy=findmax(a_list) #finding max
    miny=findmin(a_list) #finding min
    oled.fill(0) #clearing before display
    oled.text("Max: "+str(int(maxy))+" Min: "+str(int(miny)),0,0) #getting the first line ready
    #making a four pixel line of each data point that was collected
    for i in range(len(a_list)):
        oled.pixel(horizontal_pos,60-int(a_list[i]),1)
        horizontal_pos+=1
        oled.pixel(horizontal_pos,60-int(a_list[i]),1)
        horizontal_pos+=1
        oled.pixel(horizontal_pos,60-int(a_list[i]),1)
        horizontal_pos+=1
        oled.pixel(horizontal_pos,60-int(a_list[i]),1)
        horizontal_pos+=1
        #the pixel explaination pixel(x-pos,y-pos,1 to turn on the lights)
        #we start at sixty as the lowest pixel and subtract values as integers to show higher temperatures
    oled.show() #showing the display we setup

def pointit(data_list,positions): #a function to make ther servo motor point to the hottest object
    maxy=findmax(data_list) #finding max
    miny=findmin(data_list) #finding min
    pointy=data_list.index(maxy) #gettign the position in the temperature list that contains the max value
    servo_point=positions[pointy] #making the servo motor point to the position with an index matching the max 
    servo.duty(servo_point) #this points the motor to the position with the highest temp
print("All functions made fine!")

#storage variables
motor_pos=[] #where we have been
ambient_hold=[] #the ambient temp at this pos
read_hold=[] #the temperature of object here
#multiple scans
ambient_hold1=[] #the ambient temp at this pos
read_hold1=[] #the temperature of object here
ambient_hold2=[] #the ambient temp at this pos
read_hold2=[] #the temperature of object here
ambient_hold3=[] #the ambient temp at this pos
read_hold3=[] #the temperature of object here
print("Variables made!")

#servo motor happy range is 45-180; let's collect data now!
for i in range(45,181,5): #this will collect a total of 27 data points, or it should..
    servo.duty(i) #positioning the motor
    motor_pos.append(i) #we append the value of the angle that the motor is at when data is collected
    #ambient_hold.append(sensor.read_ambient_temp())
    a1=sensor.read_ambient_temp()
    time.sleep(0.1)
    a2=sensor.read_ambient_temp()
    time.sleep(0.1)
    a3=sensor.read_ambient_temp()
    time.sleep(0.1)
    am_avg=(int(a1)+int(a2)+int(a3))/3
    ambient_hold1.append(am_avg) #ambient temp avg
    #read_hold.append(sensor.read_object_temp())
    r1=sensor.read_object_temp()
    time.sleep(0.1)
    r2=sensor.read_object_temp()
    time.sleep(0.1)
    r3=sensor.read_object_temp()
    time.sleep(0.1)
    r_avg=(int(r1)+int(r2)+int(r3))/3
    read_hold1.append(r_avg) #object temperature average
    time.sleep(0.5) #pausing for half a second, so that everythign works
print("Data has been collected once")

for i in range(45,181,5): #this will collect a total of 27 data points, or it should..
    servo.duty(i) #positioning the motor
    #ambient_hold.append(sensor.read_ambient_temp())
    a1=sensor.read_ambient_temp()
    time.sleep(0.1)
    a2=sensor.read_ambient_temp()
    time.sleep(0.1)
    a3=sensor.read_ambient_temp()
    time.sleep(0.1)
    am_avg=(int(a1)+int(a2)+int(a3))/3
    ambient_hold2.append(am_avg) #ambient temp avg
    #read_hold.append(sensor.read_object_temp())
    r1=sensor.read_object_temp()
    time.sleep(0.1)
    r2=sensor.read_object_temp()
    time.sleep(0.1)
    r3=sensor.read_object_temp()
    time.sleep(0.1)
    r_avg=(int(r1)+int(r2)+int(r3))/3
    read_hold2.append(r_avg) #object temperature average
    time.sleep(0.5) #pausing for half a second, so that everythign works
print("Data has been collected twice")
    
for i in range(45,181,5): #this will collect a total of 27 data points, or it should..
    servo.duty(i) #positioning the motor
    #ambient_hold.append(sensor.read_ambient_temp())
    a1=sensor.read_ambient_temp()
    time.sleep(0.1)
    a2=sensor.read_ambient_temp()
    time.sleep(0.1)
    a3=sensor.read_ambient_temp()
    time.sleep(0.1)
    am_avg=(int(a1)+int(a2)+int(a3))/3
    ambient_hold3.append(am_avg) #ambient temp avg
    #read_hold.append(sensor.read_object_temp())
    r1=sensor.read_object_temp()
    time.sleep(0.1)
    r2=sensor.read_object_temp()
    time.sleep(0.1)
    r3=sensor.read_object_temp()
    time.sleep(0.1)
    r_avg=(int(r1)+int(r2)+int(r3))/3
    read_hold3.append(r_avg) #object temperature average
    time.sleep(0.5) #pausing for half a second, so that everythign works
print("Data has been collected thrice")

#averaging the scans
for i in range(len(motor_pos)):
    asummy=ambient_hold1[i]+ambient_hold2[i]+ambient_hold3[i]
    a_vg=asummy/3
    ambient_hold.append(a_vg)
    rsummy=read_hold1[i]+read_hold2[i]+read_hold3[i]
    r_vg=rsummy/3
    read_hold.append(r_vg)
print("Averaging the scans has completed")

#displaying results on the OLED and finding highest temp
printit(read_hold) #calling the printit function on the read object values
pointit(read_hold,motor_pos) #calling the pointit function on the read object values and motor_pos values
print("Check that everythign looks good!") 

#What's going on:
#So, my device works reasonably well so far. It can tell that my hand is a higher temperature than the room
#and it can creates a plot of the temperatures that it read
#the main issues are to do with just the mechanics of it
#The sensor is mounted to a plastic frame, and teh wires behind the sensor interfere with the range of motion
#of the sensor and where I can position it and the motor

#I performed a test of accuracy on my device, btu because of how long I have teh scans set for
#and me being impatient, I only performed four tests at each angle.
#At angle 78, the tests were 100% accurate- getting 4 out of four
#At angle 97, the tests were 75% accurate, but that may be because I a friend was sitting near the cup.
#At angle 59, the tests were 100% accurate, so it's likely my friend sitting nearby may have made it difficult.
#At angle 115, the tests were 50% accurate.
#At angle 40, the tests were 75% accurate
