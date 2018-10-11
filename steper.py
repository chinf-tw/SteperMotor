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

# forward_seq = ['1000', '1100', '0100', '0100', '0010', '0011', '0001', '0100']
# forward_seq = ['1010', '0110', '0101', '1001']
forward_seq = ['1100', '0110', '0011', '1001']
reverse_seq = ['1001', '0011', '0110', '1100']

def forward(delay, steps):
    for i in range(steps):
        for step in forward_seq:
            set_step(step)
            print(delay)
            time.sleep(delay)
            

def forward_single(delay):
    for step in forward_seq:
        set_step(step)
        time.sleep(delay)
        print(delay)


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

def NonlinearSpeed(steps):
    """geometric progression"""
    d = 0
    NonlinearStep = 0
    keepStep = 0
    
    if steps < 500:
        print("steps < 500")
        d = steps/100
        NonlinearStep = int(40/d) + 1
        print("NonlinearStep : ",NonlinearStep)
        keepStep = steps - NonlinearStep * 2
        print("keepStep : ", keepStep)
        


    for delay in range(50,10,-(NonlinearStep)):
        # forward(delay,1)
        forward_single(delay/1000)
        
        pass

    forward(10/1000,keepStep)
    

    for delay in range(10,50,NonlinearStep):
        # forward(delay,1)
        forward_single(delay/1000)
        pass

try:
    while True:
        set_step('0000')
        # delay = raw_input("Delay between steps (milliseconds)?")
        steps = input("How many steps forward? ")
        NonlinearSpeed(int(steps))
        # print(int(steps))
        # forward(int(delay) / 1000.0, int(steps))
        
        set_step('0000')
        steps = input("How many steps backwards? ")
        NonlinearSpeed(int(steps))
        # backwards(int(delay) / 1000.0, int(steps))
except KeyboardInterrupt:
    GPIO.cleanup()
    pass
    


