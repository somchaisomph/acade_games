import RPi.GPIO as GPIO

#GPIO Numbering
SWITCH_A = 26
SWITCH_B = 19
SWITCH_C = 13
SWITCH_D = 6
SWITCH_E = 5

GPIO.setmode(GPIO.BCM)


def my_callback_a(gpio):
	print "a"
	print "=========="

def my_callback_b(gpio):
	print "b"
	print "=========="

def my_callback_c(gpio):
	print "c"
	print "=========="

def my_callback_d(gpio):
	print "d"
	print "=========="

def my_callback_e(gpio):
	print "e"
	print "=========="

GPIO.setup(SWITCH_A,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_B,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_C,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_D,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SWITCH_E,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
input_a = GPIO.input(SWITCH_A)
input_b = GPIO.input(SWITCH_B)
input_c = GPIO.input(SWITCH_C)
input_d = GPIO.input(SWITCH_D)
input_e = GPIO.input(SWITCH_E)
GPIO.add_event_detect(SWITCH_A, GPIO.RISING , callback=my_callback_a,bouncetime=200)
GPIO.add_event_detect(SWITCH_B, GPIO.RISING , callback=my_callback_b,bouncetime=200)
GPIO.add_event_detect(SWITCH_C, GPIO.FALLING , callback=my_callback_c,bouncetime=200)
GPIO.add_event_detect(SWITCH_D, GPIO.FALLING , callback=my_callback_d,bouncetime=200)
GPIO.add_event_detect(SWITCH_E, GPIO.FALLING , callback=my_callback_e,bouncetime=200)



while True:
	pass

GPIO.remove_event_detect(SWITCH_A)
GPIO.remove_event_detect(SWITCH_B)
GPIO.remove_event_detect(SWITCH_C)
GPIO.remove_event_detect(SWITCH_D)
GPIO.remove_event_detect(SWITCH_E)
GPIO.cleanup([SWITCH_A,SWITCH_B,SWITCH_C,SWITCH_D,SWITCH_E])
