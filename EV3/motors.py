#!/usr/bin/env python3

from time import sleep
import os
import sys

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.

    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)

def spinTableSpinIncrement():
    spinTable = LargeMotor(OUTPUT_A)
    spinTable.on_for_seconds(SpeedPercent(1), 2)
    debug_print("spin table turned by 1 increment")

def pivotMoveUpIncrement():
    upPivot = LargeMotor(OUTPUT_B)
    upPivot.polarity = "inversed"
    upPivot.on_for_seconds(SpeedPercent(2), 1)
    upPivot.polarity = "normal"
    debug_print("pivot moved up by 1 increment")
    sleep(1)
    
def pivotMoveDownIncrement():
    upPivot = LargeMotor(OUTPUT_B)
    upPivot.polarity = "normal"
    upPivot.on_for_seconds(SpeedPercent(2), 1)
    upPivot.polarity = "inversed"
    debug_print("pivot moved down by 1 increment")
    sleep(1)

def main():
    for i in range(10):
        pivotMoveUpIncrement()
    for i in range(10):
        pivotMoveDownIncrement()
    for i in range(10):
        spinTableSpinIncrement()
    debug_print("program finished")
    return 0
    


if __name__ == '__main__':
    main()