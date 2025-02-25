def last_num():
    
    n = int(input('请输入人数：'))
    k = int(input('请输入从第几个人开始报数：'))
    c = []
    for i in range(1, n + 1):
        c.append(i)
    num = 1
    while len(c) != 1:
        c.append(c.pop(0))  
        num += 1
        if num == k:
            del c[0]  
            num = 1   
    print('输出最后留下人的号码：%s' %c)
 
last_num()