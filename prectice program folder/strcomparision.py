str1 = "manish"
str2 = "ranu"
list = []
for i in str1:
    for j in str2:
        if i == j:
            print(i,"is in str2")
            list.append(i)
        else:
            print(i,"is not in str2")
print(list,"is in str2")