from functools import reduce

sum = lambda a , b : a+b

list = [1,2,3,4,5]

val = reduce(sum , list)
print(val)