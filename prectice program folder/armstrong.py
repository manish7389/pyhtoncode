# num = 152
# c = str(num)
# n = len(c)
# count = 0
# for i in c:
#     d = i
#     e = int(d)
#     count = count + (e*e*e)
# print(count)
# if num == count:
#     print(num, " is a arrmstrong number ")
# else:
#     print(num," is not a arrmstrong number")

num1 = 900
list = []
for num2 in range(100,num1+1):
    num = num2
    c = str(num)
    n = len(c)
    count = 0
    for i in c:
        d = i
        e = int(d)
        count = count + (e*e*e)
    # print(count)
    if num == count:
        list.append(num)
        print(num, " is a arrmstrong number ")
    # else:
        # print(num," is not a arrmstrong number")   
print(list)

