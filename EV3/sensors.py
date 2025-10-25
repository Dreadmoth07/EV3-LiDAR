#!/usr/bin/env python3
from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.led import Leds

IR = InfraredSensor()

#                   array
def calculatePoint(point):
    point = [0,0,0]
    distance = 0
    rotation = 0
    elevation = 0
    distance = getDistance
    return point

def getDistance():
    d = 0
    d = IR.proximity
    while True:
        d = 100 - IR.proximity
        print("Distance", d)
        sleep(0.2)    

def rotatePoint(point, degrees):
    pass

def elevation():
    pass
    
def main():
    getDistance()
    return 0


if __name__ == '__main__':
    main()