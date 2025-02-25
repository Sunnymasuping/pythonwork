from machine import Pin
from machine import Timer
from time import sleep_ms
import machine
import time
import bluetooth

BLE_MSG = ""

p1 = Pin(22, Pin.OUT)
p2 = Pin(23, Pin.OUT)
yellow_led = Pin(19, Pin.OUT)  # 黄灯引脚
green_led = Pin(21, Pin.OUT)  # 绿灯引脚
red_led = Pin(18, Pin.OUT)  # 红灯引脚

# 设置PWM引脚和频率
ENA_PIN = 17
PWM_FREQ = 1000

ena_pwm = machine.PWM(Pin(ENA_PIN), freq=PWM_FREQ)


class ESP32_BLE():
    def __init__(self, name):
        self.led = Pin(2, Pin.OUT)
        self.timer1 = Timer(0)
        self.name = name
        self.ble = bluetooth.BLE()
        self.ble.active(True)
        self.ble.config(gap_name=name)
        self.disconnected()
        self.ble.irq(self.ble_irq)
        self.register()
        self.advertiser()

    def connected(self):
        self.led.value(1)
        self.timer1.deinit()

    def disconnected(self):        
        self.timer1.init(period=100, mode=Timer.PERIODIC, callback=lambda t: self.led.value(not self.led.value()))

    def ble_irq(self, event, data):
        global BLE_MSG
        if event == 1: #_IRQ_CENTRAL_CONNECT 手机链接了此设备
            self.connected()
        elif event == 2: #_IRQ_CENTRAL_DISCONNECT 手机断开此设备
            self.advertiser()
            self.disconnected()
        elif event == 3: #_IRQ_GATTS_WRITE 手机发送了数据 
            buffer = self.ble.gatts_read(self.rx)
            BLE_MSG = buffer.decode('UTF-8').strip()
            
    def register(self):        
        service_uuid = '6E400001-B5A3-F393-E0A9-E50E24DCCA9E'
        reader_uuid = '6E400002-B5A3-F393-E0A9-E50E24DCCA9E'
        sender_uuid = '6E400003-B5A3-F393-E0A9-E50E24DCCA9E'

        services = (
            (
                bluetooth.UUID(service_uuid), 
                (
                    (bluetooth.UUID(sender_uuid), bluetooth.FLAG_NOTIFY), 
                    (bluetooth.UUID(reader_uuid), bluetooth.FLAG_WRITE),
                )
            ), 
        )

        ((self.tx, self.rx,), ) = self.ble.gatts_register_services(services)

    def send(self, data):
        self.ble.gatts_notify(0, self.tx, data + '\n')

    def advertiser(self):
        name = bytes(self.name, 'UTF-8')
        adv_data = bytearray('\x02\x01\x02') + bytearray((len(name) + 1, 0x09)) + name
        self.ble.gap_advertise(100, adv_data)
        print(adv_data)
        print("\r\n")


def buttons_irq(pin):
    led.value(not led.value())
    print('LED is ON.' if led.value() else 'LED is OFF')
    ble.send('LED is ON.' if led.value() else 'LED is OFF')
    

def set_motor_speed(speed):
    # 设置电机速度
    ena_pwm.duty(speed)

def mark1():
    p1.on()
    p2.off()
    set_motor_speed(1023)
    time.sleep(1)

def mark2():
    p1.on()
    p2.off()
    set_motor_speed(512)
    time.sleep(1)
    
def mark3():
    p1.on()
    p2.off()
    set_motor_speed(256)
    time.sleep(1)

def stopFan():
    p1.off()
    p2.off()
    set_motor_speed(0)
    time.sleep(1)
    
def reset():
    yellow_led.value(0)  
    green_led.value(0)
    red_led.value(0)

if __name__ == "__main__":
    ble = ESP32_BLE("马苏平")

    # 检测boot按键
    but = Pin(0, Pin.IN)
    but.irq(trigger=Pin.IRQ_FALLING, handler=buttons_irq)

    # 控制蓝色led
    led = Pin(2, Pin.OUT)

    while True:
        if BLE_MSG == 'read_LED':
            print(BLE_MSG)
            BLE_MSG = ""
            print('LED is ON.' if led.value() else 'LED is OFF')
            ble.send('LED is ON.' if led.value() else 'LED is OFF')
        elif BLE_MSG:
            print("接收到的信息：>>%s<<" % BLE_MSG)
            if BLE_MSG == "!B11:":  # 按下app上数字1
                stopFan()
                reset()
            elif BLE_MSG == "!B516":  # 按下app上up键
                mark1()
                reset()
                red_led.value(1)
            elif BLE_MSG == "!B714":  # 按下app上left键
                mark2()
                reset()
                yellow_led.value(1)
            elif BLE_MSG == "!B813":  # 按下app上right键
                mark3()
                reset()
                green_led.value(1)
            BLE_MSG = ""
        sleep_ms(100)
