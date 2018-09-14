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

dataput = input('請輸入想輸出的點位：\n')

GPIO.output(a1_pin, dataput[0] == '1')
GPIO.output(a2_pin, dataput[1] == '1')
GPIO.output(b1_pin, dataput[2] == '1')
GPIO.output(b2_pin, dataput[3] == '1')
GPIO.output(en, dataput[4] == '1')

pwm = GPIO.PWM(12, 50)
pwm.start(50)
input('輸入結束'')
pwm.stop()
GPIO.cleanup()