def fun(str):
    if str=='yes' or str=='YES' or str=='Yes':
        return 'Yes'
    else:
        return 'no'
    
    
    
    
str1=str(input("enter the string:"))
print(fun(str1))
