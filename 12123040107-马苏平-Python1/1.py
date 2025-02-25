def average():
    
    s = eval(input("求平均，请输入自然数列表："))  # 输入自然数的列表
    sum = 0
    for i in s:
        sum += i
    avg=sum/len(s)
    print('%.3f'%avg)
 
average()

