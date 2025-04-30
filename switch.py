import RPi.GPIO as GPIO
from time import sleep

LED=8
Switch=10
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)

try:
   while True:
       if GPIO.input(Switch) == GPIO.HIGH:
           print("LED ON")
           GPIO.output(LED, GPIO.HIGH)
       else:
          print("LED OFF")
          GPIO.output(LED, GPIO.LOW)
          sleep(1)

finally:
     GPIO.cleanup()  
