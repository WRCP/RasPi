import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BOARD)
GPIO.setup (7, GPIO.OUT)
while True:
        GPIO.setup (7, 1)
        time.sleep (0.1)
        GPIO.setup (7, 0)      
        time.sleep (0.01)
