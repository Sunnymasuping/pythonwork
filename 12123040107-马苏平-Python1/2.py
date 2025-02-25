def descending():
   
    s = eval(input("降序，请输入自然数列表："))  # 输入自然数的列表
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            if s[i] < s[j]:
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
    print (s)
 
descending()
 
