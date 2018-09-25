#!/usr/bin/env python
import os, random
import sys
import time
from time import sleep

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) #RED B = ANGER 
GPIO.setup(17, GPIO.OUT) #RED L = ANGER

GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) #BLUE B = SADNESS 
GPIO.setup(22, GPIO.OUT) #BLUE L = SADNESS

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #YELLOW B = JOY 
GPIO.setup(24, GPIO.OUT) #YELLOW L = JOY 

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) #GREEN B = FEAR 
GPIO.setup(5, GPIO.OUT) #GREEN L = FEAR

def rndanger (): #RED
	GPIO.output(17, GPIO.HIGH)
        randomfile = random.choice(os.listdir("/home/pi/Documents/AudioClips/ANGER"))
        file = '/home/pi/Documents/AudioClips/ANGER/' + randomfile
        os.system('mpg123 ' + file)
	sleep(0.5)
	GPIO.output(17, GPIO.LOW)

def rndsadness (): #BLUE
	GPIO.output(22, GPIO.HIGH)
	randomfile = random.choice(os.listdir("/home/pi/Documents/AudioClips/SADNESS/"))
	file = '/home/pi/Documents/AudioClips/SADNESS/' + randomfile
	os.system ('mpg123 ' + file)
        sleep(0.5)
        GPIO.output(22, GPIO.LOW)

def rndhappiness (): #YELLOW
	GPIO.output(24, GPIO.HIGH)
	randomfile = random.choice(os.listdir("/home/pi/Documents/AudioClips/HAPPINESS/"))
	file = '/home/pi/Documents/AudioClips/HAPPINESS/' + randomfile
	os.system ('mpg123 ' + file)
        sleep(0.5)
        GPIO.output(24, GPIO.LOW)

def rndfear (): #GREEN
	GPIO.output(5, GPIO.HIGH)
        randomfile = random.choice(os.listdir("/home/pi/Documents/AudioClips/FEAR/"))
        file = '/home/pi/Documents/AudioClips/FEAR/' + randomfile
        os.system ('mpg123 ' + file)
        sleep(0.5)
        GPIO.output(5, GPIO.LOW)

while True:
	if (GPIO.input(4) == False): #RED/ANGER
                rndanger ()
                sleep(0.1)

	if (GPIO.input(27) == False): #BLUE/SADNESS
		rndsadness ()
		sleep(0.1)

        if (GPIO.input(23) == False): #YELLOW/HAPPINESS
                rndhappiness ()
                sleep(0.1)

	if (GPIO.input(25) == False): #GREEN/FEAR
		rndfear ()
		sleep(0.1)
