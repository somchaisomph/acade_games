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
input_b = GPIO.input(SWITCH_B)
input_c = GPIO.input(SWITCH_C)
input_d = GPIO.input(SWITCH_D)

while True:
	if GPIO.input(SWITCH_A) :
		print "A Released"
	else:
		print "A Pressed"

	if GPIO.input(SWITCH_B) :
		print "B Released"
	else:
		print "B Pressed"

	if GPIO.input(SWITCH_C) :
		print "C Released"
	else:
		print "C Pressed"
		
	if GPIO.input(SWITCH_D) :
		print "D Released"
	else:
		print "D Pressed"


GPIO.cleanup([SWITCH_A,SWITCH_B,SWITCH_C,SWITCH_D])
