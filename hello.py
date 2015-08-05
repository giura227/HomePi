#! /usr/bin/python

import RPi.GPIO as GPIO
import subprocess
from datetime import datetime

PIN = 26

def sensePerson():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIN, GPIO.IN)
    ans = GPIO.input(PIN)
    GPIO.cleanup()
    return ans

def main():
    if sensePerson():
        now = datetime.now()
        with open("speakerdata") as f:
            prev = datetime.strptime(f.read(),"%c")
        dt = now - prev
        if dt.total_seconds() > 3600 * 6:
            if now.hour > 6 and now.hour < 10:
                subprocess.call("aplay -D hw:1,0 /home/pi/HomePi/goodmorning.wav",shell=True)
            elif now.hour > 16:
                subprocess.call("aplay -D hw:1,0 /home/pi/HomePi/comehome.wav",shell=True)
        with open("speakerdata",'w') as f:
            f.write(now.strftime("%c"))

if __name__ == '__main__':
    main()
