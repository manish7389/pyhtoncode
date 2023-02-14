a = 55 #global variabal
def fun1():
    global a
    print(a)
    a = 7 # local variable
    print(a)

fun1()
print(a)