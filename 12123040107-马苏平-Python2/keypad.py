from machine import Pin
import time

r = [12,14,27,26]
c = [25,33,32,35]
row_list = [Pin(i,Pin.OUT) for i in r]  
col_list = [Pin(i,Pin.IN,Pin.PULL_DOWN) for i in c]  # 将创建的列对象放到list里面
 

names = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]
 
while True:

    for i, row in enumerate(row_list):  
        for temp in row_list:  
            temp.value(0)  
        row.value(1)
        time.sleep_ms(10)  
        for j, col in enumerate(col_list):  
            if col.value() == 1:
                print(keyboard[i][j],'被按下')
                time.sleep(0.02)
                #time.sleep_ms(20)
               