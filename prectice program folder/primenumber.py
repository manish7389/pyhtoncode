# num = int(input("enter your number"))
# num1 = 17
# if num1 > 2:
#     if num1%2 != 0:
#         print(num1,"it is a prime number")
#     else:
#         print(num1, "it is a not prime number")
# else:
#     print("it is a prime number")
# **********************************|||||||||||||||||||||||****************************
# num = 100
# if num > 0:
#     for i in range(1,num+1):
#         if i > 1:
#             for j in range(2,i):
#                 if i % j == 0:
#                     break
#             else:
#                 print(i)           
# else:
#     print("nagative number prime is not possible")

# **********************************|||||||||||||||||||||||****************************

# num = 11
# count = 0 
# i = 1
# while(i<=num):
#     if num%i == 0:
#         count = count+1
#     i = i+1

# if count==2:
#     print(num , "is prime number")
# else:
#     print(num, "is not a prime number")


# 
# **********************************|||||||||||||||||||||||****************************

# num = 6
# for i in range(2, num):
#     if num % i == 0:
#         print("not prime")
#         break

# else:
#     print("it is a prime number")

# num = 50 
# for i in range(1,num+1):
#     if i > 1:
#         for j in range(2,i):
#             if i%j == 0:
#                 break
#         else:
#             print(i)

# **********************************|||||||||||||||||||||||****************************

num1 = 1
num2 = 100
list = []
for i in range(num1,num2+1):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count = count+1
            break
    if count == 0:
        list.append(i)
print(list)


# num1 = 1
# num2 = 300
# sum = 0
# for i in range(num1,num2+1):
#     sum = sum+i

# print(sum)
