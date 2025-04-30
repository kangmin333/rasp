import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 11

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)

try:
	while True:
		key = int(input("press key 1 or 0"))
		if key == 1:
			GPIO.output(LED, GPIO.HIGH)
		elif key == 0:
			GPIO.output(LED, GPIO.LOW)

finally:
	GPIO.cleanup()
