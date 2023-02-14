# def func1(a):
#     return a+5

# num=func1(5)
# print(num)
func1 = lambda a : a+5
func2 = lambda x : x*x
func3 = lambda a,b,c : a+b+c
x = 5
print(func1(x))
print(func2(x))
print(func3(x,2,3))