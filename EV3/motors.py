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

def spinTableSpinIncrement(spinTable, upPivot):
    spinTable = LargeMotor(OUTPUT_A)
    spinTable.wait_until_not_moving()
    spinTable.on_for_degrees(SpeedPercent(1), 9) # 5 degrees with gear ratios
    #debug_print("spin table turned by 5 degrees")

def pivotMoveUpIncrement(spinTable, upPivot):
    upPivot = LargeMotor(OUTPUT_B)
    upPivot.wait_until_not_moving()
    upPivot.polarity = "normal"
    upPivot.on_for_seconds(SpeedPercent(2), 1)
    #upPivot.polarity = "normal"
    debug_print("pivot moved up by 1 increment")
    sleep(5)
    
def pivotMoveDownIncrement(spinTable, upPivot):
    upPivot = LargeMotor(OUTPUT_B)
    upPivot.wait_until_not_moving()
    upPivot.polarity = "inversed"
    upPivot.on_for_seconds(SpeedPercent(2), 1)
    #upPivot.polarity = "inversed"
    debug_print("pivot moved down by 1 increment")
    sleep(1.5)

def continuousMoveDown(spinTable, upPivot):
    upPivot = LargeMotor(OUTPUT_B)
    upPivot.wait_until_not_moving()
    upPivot.polarity = "inversed"
    upPivot.on_for_seconds(SpeedPercent(2),10)
    debug_print("pivot moved down continuously for 10 seconds")
    sleep(1.5)

def continuousMoveUp(spinTable, upPivot):
    upPivot = LargeMotor(OUTPUT_B)
    upPivot.wait_until_not_moving()
    upPivot.polarity = "normal"
    upPivot.on_for_seconds(SpeedPercent(2),5)
    debug_print("pivot moved up continuously for 10 seconds")
    sleep(1)

def main():
    for i in range(10):
        pivotMoveUpIncrement(0)
    
    debug_print("program finished")
    return 0
    


if __name__ == '__main__':
    main()