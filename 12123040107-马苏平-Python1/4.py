def max_abs():
  
    s = eval(input("取绝对值最大值，请输入数字列表："))  # 输入数字的列表
    max=s[0]
    for i in s:
        if abs(max)<abs(i):
            max=i
    print(max)
 
max_abs()

