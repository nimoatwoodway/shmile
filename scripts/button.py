#import RPi.GPIO as GPIO
#import time
#import urllib2
#
#GPIO.setmode(GPIO.BCM)
#
#GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#
#
#
#while True:
#    input_state = GPIO.input(18)
#    if input_state == False:
#        print('Button Pressed')
#        urllib2.urlopen('http://localhost:3000/click')
#        time.sleep(0.2)
#
#
import time
import RPi.GPIO as GPIO
import urllib2

PIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(PIN, GPIO.FALLING)
    print "Pressed"
    start = time.time()
    time.sleep(0.2)

    while GPIO.input(PIN) == GPIO.LOW:
        time.sleep(0.01)
    length = time.time() - start
    print length

    if length > 10:
        print "10 Sec. Press"
        from subprocess import call
	call("sudo shutdown -h now", shell=True)
    if length > 5:
        print "5 Sec. Press"
        from subprocess import call
	call("sudo shutdown -r now", shell=True)
    else:
        print "Short Press"
        urllib2.urlopen('http://localhost:3000/click')
