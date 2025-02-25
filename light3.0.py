from machine import Pin,PWM
import time


pinR = Pin(12,Pin.OUT)
pinY = Pin(14,Pin.OUT)
pinG = Pin(27,Pin.OUT)



pinR.on()
pinY.off()
pinG.off()
time.sleep(2)
pinR.off()
pinY.on()
pinG.off()
time.sleep(2)
pinR.off()
pinG.on()
time.sleep(2)
pinG.off
