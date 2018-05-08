from gpiozero import LED
#from time import sleep
import time

led = LED(17)



def increasing_blink():
    for i in range(6000):
        led.off()
        i+=1
    for i in range(500):
        led.on()
        i+=1
    

while True:
    increasing_blink()

