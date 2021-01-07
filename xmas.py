#!/usr/bin/env python3
#-- coding: utf-8 --

import RPi.GPIO as GPIO
import time
import random


def launchXMAS(pins, onChance, frequency):

    # Enable GPIOs control as outputs
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

    while 1:
        pin = pins[random.randrange(len(pins))]
        # Switch on
        if random.randint(1,100) <= onChance:
            GPIO.output(pin, GPIO.HIGH)

        # Switch off
        else:
            GPIO.output(pin, GPIO.LOW)
        time.sleep(frequency)


if __name__ == '__main__':

    # GPIO init
    GPIO.setmode(GPIO.BOARD) # Enable 'board' mode
    GPIO.setwarnings(False) # Disable alert messages

    pins=[33,35,36,37,38,40]

    onChance = 50 # Percent of chance to switch a LED (described to the pin number) on
    frequency = 0.2 # Frequancy of the attack loop

    # Launch the basic cycle by default
    launchXMAS(pins, onChance, frequency)