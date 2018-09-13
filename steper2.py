import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

en = 12
a1_pin = 17
a2_pin = 27
b1_pin = 23
b2_pin = 24
GPIO.setup(en, GPIO.OUT)
GPIO.setup(a1_pin, GPIO.OUT)
GPIO.setup(a2_pin, GPIO.OUT)
GPIO.setup(b1_pin, GPIO.OUT)
GPIO.setup(b2_pin, GPIO.OUT)

GPIO.output(en, GPIO.HIGH)

GPIO.output(a1_pin, GPIO.HIGH)
GPIO.output(a2_pin, GPIO.LOW)
GPIO.output(b1_pin, GPIO.HIGH)
GPIO.output(b2_pin, GPIO.LOW)

isY = raw_input("return 'Y' to GPIO.cleanup")
if isY == "Y":
    GPIO.cleanup()