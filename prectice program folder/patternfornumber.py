n = 5 
p = 1
for i in range(n):
    for j in range(i,n):
        print(p,end=" ")
        p = p+1
    p = 1
    print(" ")

# *************************************************************************

# n = 5
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print(p,end=" ")
#         p = p+1
#     p = 1
#     print(" ")

# *************************************************************************
# n = 5 
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#         p = p+1
#     p = 1

#     print(" ")

# *************************************************************************

# n = 5 
# p = 5
# for i in range(n):
#     for j in range(i+1):
#         print(p,end=" ")
#         p = p-1
#     p = 5

#     print(" ")

# *************************************************************************

n = 5 
k = 5
for i in range(n):
    p = k
    for j in range(i+1):
        print(p,end=" ")
        p = p+1
    k = k-1

    print(" ")