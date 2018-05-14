from gpiozero import LED, Button
from time import sleep

led = LED(19)
button = Button(16)

button.wait_for_press()
led.on()
sleep(3)
led.off()
