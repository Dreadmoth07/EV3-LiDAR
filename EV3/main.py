#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

import motors
import sensors


def main():
    file = open("test.txt", "w")
    spinTable = LargeMotor(OUTPUT_A)
    upPivot = LargeMotor(OUTPUT_B)
    for i in range(7):
        listToWrite = ""
        allEmpty = True
        for j in range(36):
            spinTable.wait_until_not_moving()
            currentPoint = sensors.calculatePoint(0.8*i, j*10) #each elevation is on average 0.8cm
            if (not(currentPoint[0] == currentPoint[2] and currentPoint[0] == 0)): # is it not an empty point
                allEmpty = False
            for k in range(3):
                number = round(currentPoint[k],3)
                if k == 2:
                    listToWrite+= str(number)
                else:
                    listToWrite+= str(number) + " "
            
            listToWrite+="\n"
            motors.spinTableSpinIncrement(spinTable, upPivot)
            motors.debug_print("Table moved by 5 degrees for the", j, "th time on cycle", i)
        if(not(allEmpty)):
            file.write(listToWrite)
            file.write("\n")
            
        motors.pivotMoveUpIncrement(spinTable, upPivot)

    motors.continuousMoveDown(spinTable, upPivot)


    file.close()
    return 0


if __name__ == '__main__':
    main()