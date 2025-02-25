def add_n():
  
    n, a = map(int, input('请输入两个正整数(用空格隔开)：').split())
    flag = 0
    m = a
    sum = int(0)
    for i in range(1, n + 1):
        sum += m
        if flag == 0:
            print(m, end=" ")
        else:
            print("+ {}".format(m), end=" ")
        m = 10 * m + a
        flag += 1
    print("= %u" %sum)           
 
add_n()