# num = int(input("enter your number : "))
# if(num>=10):
#     print("num is gretter than 10 ")
# elif(num>=20):
#     print("num is gretter than 20 ")
# else:
#     print("num is less than 10")
num1 = int(input("enter number 1 :"))
num2 = int(input("enter number 2 :"))
num3 = int(input("enter number 3 :"))
num4 = int(input("enter number 4 :"))
if(num1<num2):
    a1 = num2
else:
    a1 = num1
if(num3<num4):
    a2 = num4
else:
    a2 = num3
if(a1<a2):
    print("gretter number is : ", a2)
else:
    print("gretter number is : ", a1)