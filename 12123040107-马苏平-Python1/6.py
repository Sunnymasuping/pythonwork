def inner_product():

    print("输入两个包含若干整数的等长列表，输出两内积")
    s1 = eval(input("请输入整数列表："))
    s2 = eval(input("请输入与上等长的整数列表："))
    m=[]
    for i in range(0,len(s1)):
        m.append(s1[i]*s2[i])
    print(m)
 
inner_product()
 