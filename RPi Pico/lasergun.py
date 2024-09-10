from machine import Pin
from time import sleep

laser = Pin(15, Pin.OUT)
laser.off()
button = Pin(14, Pin.IN, Pin.PULL_DOWN)
button_pressed = False

while True:
    if button.value() and not button_pressed:
        button_pressed = True
        laser.on()
        sleep(0.2)
        laser.off()
    if not button.value() and button_pressed:
        button_pressed = False
        

GPIO.cleanup()
