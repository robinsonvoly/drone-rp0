#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

dc = 5

servo = GPIO.PWM(11,1000)
servo.start(dc)
print('Connect Battery & Press ENTER to start')
res = raw_input()
servo.ChangeDutyCycle(dc)
print('Press ENTER to start')
res = raw_input()

print ('Increase > a | Decrease > z | Save Wh > n | Set Wh > h | Quit > 9')

cycling = True
try:
    while cycling:
        servo.ChangeDutyCycle(dc)
        res = raw_input()
        if res == 'a':
            dc = dc + 0.05
        if res == 'z':
            dc = dc - 0.05
        if res == 'h':
            mymotor.setWh()
        if res == '9':
            cycling = False
finally:
    # Shut down
    servo.stop()
    print ("dc var setting is: ")
    print (dc)

print('Press ENTER to quit')
res = raw_input()
servo.stop()
GPIO.cleanup()