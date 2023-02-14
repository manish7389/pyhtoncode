n = 5 
temp = 1
for i in range(1,n+1):
    temp = (temp*i)

print(temp)

for i in range(n+1):
    for j in range(i,n+1):
        print(" ",end=" ")
    for k in range(i):
        print("*", end=" ")
    print(" ")