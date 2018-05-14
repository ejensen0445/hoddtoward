from gpiozero import LED, Button
from time import sleep

led = LED(19)
button = Button(16)

while True:
    button.wait_for_press()
    led.toggle()
    sleep(0.25)
    
