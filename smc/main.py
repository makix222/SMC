from gpiozero import LED
from time import sleep

yellow = LED(2)

while True:
    yellow.on()
    sleep(.5)
    yellow.off()
    sleep(.5)
