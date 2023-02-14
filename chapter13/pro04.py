# def func1(num):
#     if num%5==0:
#         return True
#     else:
#         False

list1 = [5, 10, 22, 25, 55, 78, 54, 76, 100]
val = filter(lambda a : a%5==0,list1)
print(list(val))