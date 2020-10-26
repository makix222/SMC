from gpiozero import AngularServo as angle_servo
from time import sleep

servo = angle_servo(14)

while True:
    angle = float(input("Angle?"))
    servo.angle = angle
    sleep(1)
