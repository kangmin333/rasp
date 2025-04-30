import RPi.GPIO as GPIO
import time

try:
   GPIO.setwarnings(False)
   GPIO.setmode(GPIO.BOARD)
   LED = 10
   GPIO.setup(LED, GPIO.OUT, initial = GPIO.LOW)
   
   while True:
      GPIO.output(LED, GPIO.HIGH)
      time.sleep(0.05)

      GPIO.output(LED, GPIO.LOW)
      time.sleep(0.01)

except KeyboardInterrupt:
   pass

finally:
    GPIO.cleanup()  
