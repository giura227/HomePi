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
    wd = "/home/pi/HomePi/"
    if sensePerson():
        now = datetime.now()
        with open(wd + "speakerdata") as f:
            prev = datetime.strptime(f.read(),"%c")
        dt = now - prev
        if dt.total_seconds() > 3600 * 6:
            if now.hour > 6 and now.hour < 10:
                subprocess.call("aplay -D hw:1,0 {0}goodmorning.wav".format(wd),shell=True)
            elif now.hour > 16:
                subprocess.call("aplay -D hw:1,0 {0}comehome.wav".format(wd),shell=True)
        with open(wd + "speakerdata",'w') as f:
            f.write(now.strftime("%c"))

if __name__ == '__main__':
    main()
