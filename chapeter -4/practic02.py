# store the same value in set and cheak that
num1 = int(input("enter the number : "))
num2 = int(input("enter the number : "))
num3 = int(input("enter the number : "))
num4 = int(input("enter the number : "))
num5 = int(input("enter the number : "))
num6 = int(input("enter the number : "))
num7 = int(input("enter the number : "))
num8 = int(input("enter the number : "))

s = {num1,num2,num3,num4,num5,num6,num7,num8}
print(s)
# can ve store int(18) and str("18") in set
set = {6,7,8,98}
set.add(18)
set.add("18")
print(set) #yes we can add this type of value