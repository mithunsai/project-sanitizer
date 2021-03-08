def forward():
    GPIO.output(wheel1,True)
    GPIO.output(wheel2,True)

def reverse():
    GPIO.output(wheel3,True)
    GPIO.output(wheel4,True)

def stop():
    GPIO.output(wheel1,False)
    GPIO.output(wheel2,False)
    GPIO.output(wheel3,False)
    GPIO.output(wheel4,False)

def left():
    GPIO.output(wheel2,True)
    prev=0
    count=0
    while count<20:
        state= GPIO.input(encoder2)
        if not prev == state:
            count+=1
        prev = state
    stop()

def right():

    GPIO.output(wheel1,True)
    prev=0
    count=0
    while count<20:
        state= GPIO.input(encoder1)
        if not prev == state:
            count+=1
        prev = state
    stop()

def move_vlength():
    forward()
    prev=0
    count=0
    while count<40:
        state= GPIO.input(encoder1)
        if not prev == state:
            count+=1
        prev = state
    stop()
