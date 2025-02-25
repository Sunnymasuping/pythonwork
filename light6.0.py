from machine import Pin
from time import sleep

pinR=Pin(14,Pin.OUT)
pinG=Pin(28,Pin.OUT)
pinY=Pin(12,Pin.OUT)
a = 0
while True:
    pinR.value((a % 3) % 2)
    pinG.value(((a + 1) % 3) % 2)
    pinY.value(((a + 2) % 3) % 2)
    a = a + 1
    sleep(2)
