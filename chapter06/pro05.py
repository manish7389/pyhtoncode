i =0 
while(i<=10):
    namelist = ["manish","kumar","yadav","ahir","patel"]
    name = input("please enter your name : ")
    if(name in namelist):
        print("your name is already present in list ! injoy")
    elif(name == "exit"):
        print("exit")
        break
    else:
        print("your name is not present in list please try again !")
