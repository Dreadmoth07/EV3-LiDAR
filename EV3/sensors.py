#!/usr/bin/env python3
from time import sleep
from math import cos, sin, pi

#from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor
#from ev3dev2.led import Leds

IR = InfraredSensor()

#                   array
def calculatePoint(elevation, rotation):
    #        x, y, z
    point = [0, 1, 0]
    distance = 0
    distance = getDistance()
    point[0] = distance
    point[1] = elevation
    rotatePoint(point, rotation)
    return point

def getDistance():
    d = 0
    d = 16 - IR.proximity
    #print("Distance", d)
    return d    

def rotatePoint(point, degrees):
    rad = degrees * (pi/180)
    cosDegrees = cos(rad)
    sinDegrees = sin(rad)
    x = point[0]
    z = point[2]
    point[0] = (x*cosDegrees) + (z*sinDegrees)
    point[2] = (z*cosDegrees) - (x*sinDegrees)
    point[0] = round(point[0],3)
    point[2] = round(point[2],3)
    #print(point[2])
    if point[2] == -0.0:
        point[2] = 0
    if point[0] == -0.0:
        point[0] = 0
    #print(point[2])
    #sleep(2)
    point[0] *= 0.7
    point[2] *= 0.7
    return point
    
def main():
    point = []
    while True:
        point = calculatePoint(1,270)
        print(point)
        sleep(0.5)
    return 0


if __name__ == '__main__':
    main()