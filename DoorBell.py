#!/usr/bin/env python
import os
from time import sleep
import time
import RPi.GPIO as GPIO
import Email

ruta = os.path.dirname(os.path.realpath(__file__))#'/home/pi/Desktop/DoorBell'
sound_folder = '/sound/bell2.mp3'
photo_folder = '/photo/'

gpio_in = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_in, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def bell(ruta, sound):
    print('bell')
    os.system('omxplayer ' + ruta + sound + ' &')

def photo(name):
    print('tomando foto')
    command_photo = "fswebcam -p YUYV -d /dev/video0 -r 352x288 " + ruta + name
    os.system(command_photo)

print('main')
while True:
    if(GPIO.input(gpio_in)==False):
        print(GPIO.input(gpio_in))
        print('pulsado boton')
        tmstamp = time.strftime('%Y%m%d_%H%M')
        bell(ruta, sound_folder)

        name = photo_folder + tmstamp + '_photo.jpg'
        photo(name)
        Email.sendEmail(ruta, name)
        sleep(1) #t en segundos
