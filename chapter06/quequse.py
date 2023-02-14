i=0
while i<10 :
    age = int(input("enter your age : "))
    if(age>=18):
        print("you can drink")
    elif(age==0):
        print("thanks ! for using this program")
        exit()
    else :
        print("you can not drink")