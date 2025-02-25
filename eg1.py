def fib(n)://n是形参
    a,b = 1,1
    while a < n:
        print(a,end=' ')
        a,b = b,a+b
        print()
        fib(1000)//1000是实参，fib：调用函数
         
         
f = lanbda x,y,z:x+y+z//给lambda表达式起名字
f(1,2,3)//像函数一样调用
//6

g = lambda x,y=2,z=3:x+y+z//参数默认值
g(1)
//6

