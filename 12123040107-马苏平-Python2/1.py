def factorization():
    
    list1 = []                	
    n = int(input('请输入一个正整数：'))
    for i in range(2, n):
        while i != n:
            if n % i == 0:
                list1.append(i)
                n = n / i
            else:
                break
    list1.append(int(n))
    print("输出因式分解的结果列表：%s" %list1)   
 
factorization()