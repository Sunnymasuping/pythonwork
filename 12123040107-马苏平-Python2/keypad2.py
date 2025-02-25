import machine
import utime

# 设置键盘的行和列
ROWS = [machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP),
        machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP),
        machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP),
        machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)]
COLS = [machine.Pin(25, machine.Pin.OUT),
        machine.Pin(33, machine.Pin.OUT),
        machine.Pin(23, machine.Pin.OUT),
        machine.Pin(35, machine.Pin.OUT)]

# 设置键盘的按键对应的字符
KEYS = [['1', '2', '3', 'A'],
        ['4', '5', '6', 'B'],
        ['7', '8', '9', 'C'],
        ['*', '0', '#', 'D']]

# 初始化键盘
for col in COLS:
    col.value(1)

# 读取键盘按键的函数
def read_keys():
    keys = []
    for col in range(4):
        COLS[col].value(0)
        for row in range(4):
            if ROWS[row].value() == 0:
                keys.append(KEYS[row][col])
                utime.sleep_ms(10)
        COLS[col].value(1)
    return keys

# 进行数学表达式计算的函数
def calculate_expression(expression):
    # 将表达式中的运算符替换为Python中的运算符
    expression = expression.replace('*', ' * ')
    expression = expression.replace('/', ' / ')
    expression = expression.replace('+', ' + ')
    expression = expression.replace('-', ' - ')
    # 使用eval函数进行表达式求值
    result = eval(expression)
    return result

# 读取键盘输入并进行数学表达式计算
expression = ''
while True:
    keys = read_keys()
    if '#' in keys:
        # 如果按下了#键，则计算表达式的值并输出结果
        result = calculate_expression(expression)
        print('{} = {}'.format(expression, result))
        expression = ''
    else:
        # 否则将按键对应的字符添加到表达式中
        for key in keys:
            expression += key
