#!/usr/bin/env python3

from time import sleep

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor
from ev3dev2.led import Leds

def main():
    spinTable = LargeMotor(OUTPUT_A)
    spinTable.on_for_rotations(SpeedPercent(1), 1)
    return 0


if __name__ == '__main__':
    main()