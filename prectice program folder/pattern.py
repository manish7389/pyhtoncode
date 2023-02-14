n = 5 
for i in range(n):
    p = 1
    if i == 4:
        break
    for j in range(i,n):
        print(p,end=" ")
        p = p+1

    print(" ")