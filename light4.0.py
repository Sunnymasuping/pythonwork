from machine import Pin
from time import sleep

pinX = Pin(12, Pin.IN, Pin.PULL_UP)
status = pinX.value()

while True:
    tmp_status = pinX.value()
    if status != tmp_status:
        print('changed')
    sleep(0.1)
