from machine import Pin
import time
import sys
row1 = Pin(19,Pin.OUT)
row2 = Pin(18,Pin.OUT)
row3 = Pin(5,Pin.OUT)
row4 = Pin(17,Pin.OUT)
r_list = [row1,row2,row3,row4]


col1 = Pin(16,Pin.IN,Pin.PULL_DOWN)
col2 = Pin(4,Pin.IN,Pin.PULL_DOWN)
col3 = Pin(2,Pin.IN,Pin.PULL_DOWN)
col4 = Pin(15,Pin.IN,Pin.PULL_DOWN)
c_list = [col1,col2,col3,col4]


names = [#对应间键盘的按键
        ["1", "2", "3", "A"],
        ["4", "5", "6", "B"],
        ["7", "8", "9", "C"],
        ["*", "0", "#", "D"]
        ]
a = ""
b = 0
while True:
    for i,row in enumerate(r_list):#只让对应的行通电
        for temp in r_list:
            temp.value(0)#给每一个行对象赋值
            
        row.value(1)
        time.sleep(0.1)
        for j,col in enumerate(c_list):
            if col.value() == 1:
                print("{}被按下：".format(names[i][j]))
                
                if names[i][j] != "#":
                    if names[i][j] == "A":
                        a += " + "
                    else:
                        a += names[i][j] #定义A按键为加号
                elif names[i][j] == "#":
                   
                    print(a,"= %-d" % eval(a))
                    sys.exit(0)
                
    time.sleep(0.1)



