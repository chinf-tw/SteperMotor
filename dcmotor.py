import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

inputer = 16

GPIO.setup(inputer, GPIO.OUT)

GPIO.output(inputer, GPIO.LOW)

input("return to stop")

GPIO.cleanup()