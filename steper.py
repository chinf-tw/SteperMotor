import RPi.GPIO as GPIO
import time

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
GPIO.setup(en,GPIO.OUT)

GPIO.output(en, GPIO.HIGH)

forward_seq = ['1010', '0110', '0101', '1001']
reverse_seq = ['1001', '0101', '0110', '1010']

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