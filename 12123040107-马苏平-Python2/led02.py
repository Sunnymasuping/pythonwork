from machine import Pin
from time import sleep

a = Pin(13, Pin.OUT)
b = Pin(12, Pin.OUT)
c = Pin(14, Pin.OUT)
d = Pin(27, Pin.OUT)
e = Pin(26, Pin.OUT)
f = Pin(25, Pin.OUT)
g = Pin(33, Pin.OUT)
dp = Pin(32, Pin.OUT)

led = [a,b,c,d,e,f,g,dp]


for p in led:
    p.value(1)