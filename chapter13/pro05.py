from functools import reduce
def func1(num1 , num2):
    if num1<num2 :
        return num2
    else:
        return num1
l = [1, 2, 3, 15, 5, 20, 7, 8, 10, 50,100,56,655]

val = reduce(func1,l)
print(val)
#  method - 2
a = reduce(max,l)
print(a)