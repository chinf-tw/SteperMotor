from vendor.StepMotor import StepMotor
import time
def NonlinearSpeed(steps):
    """geometric progression (200 steps = Make a turn)"""
    
    # d = 0

    
    
    isNonlinear = True
    NonlinearStep = 4
    keepStep = 0
    multiple = 1
    StartDelay = int(28 * multiple) # 4的倍數
    EndDelay = int(8 * multiple)    # 4的倍數
    # NonlinearStep = 
    # if steps < 500:
    #     print("steps < 500")
    #     d = steps/100
    #     NonlinearStep = int(40/d) + 1
    #     print("NonlinearStep : ",NonlinearStep)
    #     keepStep = steps - NonlinearStep * 2
    #     print("keepStep : ", keepStep)
    keepStep = (steps - (StartDelay - EndDelay + 1) *2) /4
    print("keepStep : ",keepStep)
    isNonlinear = keepStep > 0

    if isNonlinear:
        for delay in range(StartDelay,EndDelay-1,-(NonlinearStep)):
            forward_single(delay/(1000 * multiple))
            print("Start : ", delay)
            pass
    if isNonlinear:
        forward(8/1000,int(keepStep))
    else:
        forward(8/1000,int(steps))
    
    if isNonlinear:
        for delay in range(EndDelay,StartDelay+1,NonlinearStep):
            forward_single(delay/(1000 * multiple))
            print("End : ", delay)
            pass
steper = StepMotor()
delay = 8/1000
try:
    while True:
        
        steper.initialize()
        steper.forward(delay,300)
        time.sleep(0.2)
        steper.backward(delay,300)
        time.sleep(0.2)
        # NonlinearSpeed(1000)
except KeyboardInterrupt:
    steper.clean()
    pass