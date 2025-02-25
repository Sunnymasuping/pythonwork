from machine import Pin
from time import sleep

pinR=Pin(12,Pin.OUT)
pinG=Pin(14,Pin.OUT)
pinY=Pin(27,Pin.OUT)
a = 0
b = 1
c = 2
while True:
    pinR.value((a % 3) % 2)
    a = a + 1
    pinG.value((b % 3) % 2)
    b = b + 1
    pinY.value((c % 3) % 2)
    c = c + 1
    sleep(2)
