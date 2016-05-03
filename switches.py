import RPi.GPIO as GPIO

#GPIO Numbering
SWITCH_A = 6
SWITCH_B = 13
SWITCH_C = 19
SWITCH_D = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCH_A,GPIO.IN)
GPIO.setup(SWITCH_B,GPIO.IN)
GPIO.setup(SWITCH_C,GPIO.IN)
GPIO.setup(SWITCH_D,GPIO.IN)

input_a = GPIO.input(SWITCH_A)
input_a = GPIO.input(SWITCH_A)
while True:
	if GPIO.input(26) :
		print "Released"
	else:
		print "Pressed"

GPIO.cleanup()
