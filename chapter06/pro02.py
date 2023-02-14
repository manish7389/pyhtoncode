num1 = int(input("enter first number : "))
num2 = int(input("enter second number :"))
num3 = int(input("enter thard number :"))
p1=(num1+num2+num3)/3
print(p1)
if(num1<33):
    print("you are fail ")
elif(num2<33):
    print("you are fail ")
elif(num3<33):
    print("you are fail ")
elif(p1<40):
    print("your are fail")
else:
    print("cong you are pass !")