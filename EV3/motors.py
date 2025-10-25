#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds
def spinTableSpin():
    spinTable = LargeMotor(OUTPUT_A)
    spinTable.on_for_seconds(SpeedPercent(1), 20)

def pivotMove():
    upPivot = LargeMotor(OUTPUT_B)
    upPivot.polarity = "inversed"
    upPivot.on_for_seconds(SpeedPercent(1), 0.1)
    upPivot.polarity = "normal"
    

def main():
    pivotMove()
    return 0
    


if __name__ == '__main__':
    main()