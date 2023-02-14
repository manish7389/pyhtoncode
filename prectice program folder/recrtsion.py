# i =0
# def fun1():
#     global i
#     i = i+1
#     print(i)
#     fun1()

# fun1()

def fectorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fectorial(n-1)
    
fect = fectorial(5)
print(fect)
