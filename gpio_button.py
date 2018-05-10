from gpiozero import Button
import time

button = Button(16)

while True:
    button.wait_for_press()
    print('You pushed me!')
    time.sleep(.25)
