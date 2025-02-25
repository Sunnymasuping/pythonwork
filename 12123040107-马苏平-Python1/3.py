def digit():
   
    s = eval(input("取位数，请输入自然数列表："))  # 输入自然数的列表
    m=[]
    n=0
    for i in s:
        m.append(len(str(i)))
        n+=1
    print(m)
 
digit()
 
