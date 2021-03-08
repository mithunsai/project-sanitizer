breadth = 0
length = 0
i = 0
dis_covered=0
while breadth < total_breadth:
    if i%2 == 0:
        forward()
        while length < total_length:
            count=0
            prev = 0
            distance = 100
            while count<40 and distance > 20:
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
            dis_covered = (count/40)*22.3
            length = length + dis_covered
        stop()
        if breadth_sensor == TRIG2:
            left()
            move_vlength()
            left()
        else:
            right()
            move_vlength()
            right()
        breadth = breadth + vlength
    else:
        while length > 0:
            count=0
            prev = 0
            distance = 100
            while count<40 and distance > 20:
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
            dis_covered = (count/40)*22.3
            length = length - dis_covered
        if breadth_sensor == TRIG3:
            left()
            move_vlength()
            left()
        else:
            right()
            move_vlength()
            right()
        breadth = breadth + vlength
    i += 1
