import  RPi.GPIO as GPIO
import time
from collections import Counter

GPIO.setmode(GPIO.BOARD)

TRIG1 = 16
ECHO1= 17
TRIG2 = 18
ECHO2= 19
TRIG3= 20
ECHO3= 21
TRIG4 = 22
ECHO4= 23
wheel1= 24
wheel2=25
encoder=26
TRIG=[TRIG1,TRIG2,TRIG3,TRIG4]
ECHO=[ECHO1,ECHO2,ECHO3,ECHO4]
start= 15
distances=[]
counter_dict = Counter()

GPIO.setup(TRIG1,GPIO.OUT)
GPIO.setup(ECHO1,GPIO.IN)
GPIO.setup(TRIG2,GPIO.OUT)
GPIO.setup(ECHO2,GPIO.IN)
GPIO.setup(TRIG3,GPIO.OUT)
GPIO.setup(ECHO3,GPIO.IN)
GPIO.setup(TRIG4,GPIO.OUT)
GPIO.setup(ECHO4,GPIO.IN)
GPIO.setup(start,GPIO.IN)

GPIO.output(TRIG1, False)
GPIO.output(TRIG2, False)
GPIO.output(TRIG3, False)
GPIO.output(TRIG4, False)

time.sleep(2)




if GPIO.input(start) == 1:
    try:
        for i,j in zip(TRIG,ECHO):

            GPIO.output(i, True)
            time.sleep(0.00001)
            GPIO.output(i, False)

           while GPIO.input(j)==0:
               pulse_start = time.time()
               print("start",pulse_start)

           while GPIO.input(j)==1:
               pulse_end = time.time()
               print("end",pulse_end)

           pulse_duration = pulse_end - pulse_start

           distance = pulse_duration * 17150

           distances.append(round(distance+1.15, 2))
           counter_dict[TRIG] = distance

        list_of_large= counter_dict.most_common(2)
        length_sensor=list_of_large[0][0]
        breadth_sensor=list_of_large[1][0]
        distance=1000
        prev=0
        count=0
        forward()
        while distance>200:
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO1)==0:
               pulse_start = time.time()
               print("start",pulse_start)

            while GPIO.input(ECHO1)==1:
               pulse_end = time.time()
               print("end",pulse_end)

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150

            state= GPIO.input(encoder)
            if not prev == state:
                count+=1
            prev = state
        stop()

        dis_covered= (count/40)*22.3
        total_length = dis_covered+ distance
        reverse()
        prev = 0
        while count>0:
            state= GPIO.input(encoder)
            if not prev == state:
                count-=1
            prev = state
        stop()

        if breadth_sensor==TRIG2:
            left()
        else:
            right()

        distance=1000
        prev=0
        count=0
        forward()
        while distance>200:
            GPIO.output(TRIG1, True)
            time.sleep(0.00001)
            GPIO.output(TRIG1, False)

            while GPIO.input(ECHO1)==0:
               pulse_start = time.time()
               print("start",pulse_start)

            while GPIO.input(ECHO1)==1:
               pulse_end = time.time()
               print("end",pulse_end)

            pulse_duration = pulse_end - pulse_start

            distance = pulse_duration * 17150

            state= GPIO.input(encoder)
            if not prev == state:
                count+=1
            prev = state
        stop()
        dis_covered= (count/40)*22.3
        total_breadth = dis_covered+ distance
        reverse()
        prev = 0
        while count>0:
            state= GPIO.input(encoder)
            if not prev == state:
                count-=1
            prev = state
        stop()

        if not breadth_sensor==TRIG2:
            left()
        else:
            right()




        li=[]
        for k in range(total_length):
           l=[]
           for u in range(total_breadth):

               l.append([k,u])
           li.append(l)
        print(li)
    except Exception as e:
        print(e)











#    length=breadth=int(distance)


# except KeyboardInterrupt:
#      GPIO.cleanup()
