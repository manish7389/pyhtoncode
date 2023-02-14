list = [5, 8, 2, 3, 1, 50, 30, 10, 11]
n = len(list)
for i in range(n):
    for j in range(i+1,n):
        if list[i]>list[j]:
            list[i],list[j] = list[j], list[i]

print(list)