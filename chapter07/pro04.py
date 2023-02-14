num = int(input("enter your number : "))
prime = False
for i in range(2,num):
    if(num%i==0):
       prime = True
       break
if(prime==False):
    print("this numebr is prime")
else:
    print("this numebr is not prime")
