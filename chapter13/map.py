def func1(num):
    return num*num

l = [2,4,6]
# method-1
l2 = []

for item in l:
    l2.append(func1(item))

print(l2)

# method-2 by map function
print(list(map(func1,l)))