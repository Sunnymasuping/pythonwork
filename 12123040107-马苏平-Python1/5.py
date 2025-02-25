def product():
   
    s = eval(input("取整数乘积，请输入整数列表："))  # 输入整数列表
    p=s[0]
    for i in s:
        p=p*i
    p=int(p/s[0]) 
    print(p)
 
product()

