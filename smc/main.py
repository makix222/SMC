from gpiozero import Servo
from time import sleep

servo_pin = 14
sg90_correction = 0.45
maxPW = (2.0 + sg90_correction)/1000
minPW = (1.0 - sg90_correction)/1000

servo = Servo(servo_pin, min_pulse_width=minPW, max_pulse_width=maxPW)

while True:
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.min()
    print("min")
    sleep(1)
    servo.mid()
    print("mid")
    sleep(0.5)
    servo.max()
    print("max")
    sleep(1)
