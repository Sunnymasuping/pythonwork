from machine import Pin
from time import sleep

a = Pin(17, Pin.OUT)
b = Pin(12, Pin.OUT)
c = Pin(14, Pin.OUT)
d = Pin(27, Pin.OUT)
e = Pin(26, Pin.OUT)
f = Pin(25, Pin.OUT)
g = Pin(33, Pin.OUT)
dp = Pin(32, Pin.OUT)

led = [a,b,c,d,e,f,g,dp]

number = [
    [1,1,1,1,1,1,0,0],#0
    [0,1,1,0,0,0,0,0],#1
    [1,1,0,1,1,0,1,0],#2
    [1,1,1,1,0,0,1,0],#3
    [0,1,1,0,0,1,1,0],#4
    [1,0,1,1,0,1,1,0],#5
    [1,0,1,1,1,1,1,0],#6
    [1,1,1,0,0,0,0,0],#7
    [1,1,1,1,1,1,1,0],#8
    [1,1,1,1,0,1,1,0],#9
          ]

def show(n):
    global led, number
    for i, p in enumerate(led):
        p.value(number[n][i])
        
        
for i in range(0,10):
    show(i)
    sleep(1)
