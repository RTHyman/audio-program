import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)  
GPIO.setup(5, GPIO.OUT) 

try: 
    while True: 
        button_state = GPIO.input(25)
        if button_state == False:
            GPIO.output(5, True)
            print('Button Pressed....')
            time.sleep(0.2)
        else:
            GPIO.output(5, False)
except:
    GPIO.cleanup()
