import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
en = 12
a1_pin = 17 #A
a2_pin = 27 #B
b1_pin = 23 #/A
b2_pin = 24 #/B
GPIO.setup(en, GPIO.OUT)
GPIO.setup(a1_pin, GPIO.OUT)
GPIO.setup(a2_pin, GPIO.OUT)
GPIO.setup(b1_pin, GPIO.OUT)
GPIO.setup(b2_pin, GPIO.OUT)


GPIO.output(en, GPIO.HIGH)

forward_seq = ['0111', '1011', '1101', '1110']
reverse_seq = ['1110', '1101', '1011', '0111']

def forward(delay, steps):
    for i in range(steps):
        for step in forward_seq:
            set_step(step)
            time.sleep(delay)

def backwards(delay, steps):
    for i in range(steps):
        for step in reverse_seq:
            set_step(step)
            time.sleep(delay)

def set_step(step):
    GPIO.output(en, GPIO.HIGH)
    GPIO.output(a1_pin, step[0] == '1')
    GPIO.output(a2_pin, step[1] == '1')
    GPIO.output(b1_pin, step[2] == '1')
    GPIO.output(b2_pin, step[3] == '1')
try:
    while True:
        set_step('0000')
        delay = raw_input("Delay between steps (milliseconds)?")
        steps = raw_input("How many steps forward? ")
        forward(int(delay) / 1000.0, int(steps))

        set_step('0000')
        steps = raw_input("How many steps backwards? ")
        backwards(int(delay) / 1000.0, int(steps))
except KeyboardInterrupt:
    pass
GPIO.cleanup()