def palindrome():
   
    str1 = input("请输入一串字符串：")
    if str1[::-1] == str1:  
        print("True")
    else:
        print("False")
 
palindrome()
