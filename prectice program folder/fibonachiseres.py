n = 10 
temp = 0
for i in range(n+1):
    temp = (temp+i)

print(temp)


# **********************************************************************
n = 5
temp = 1
for i in range(1,n+1):
    temp = (temp*i)

print(temp)

# **********************************************************************
 
# n = 10 
# a = 0 
# b = 1
# print(a)
# print(b)
# for i in range(n):
#     c = a+b
#     a = b
#     b = c
#     print(c)


# **********************************************************************

def fibonnaci(n):
    a = 0 
    b = 1
    print(a)
    while (b<n):
        print(b)
        c = a+b
        a = b
        b = c
fibonnaci(150)