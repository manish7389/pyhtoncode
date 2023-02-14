a = int(input("enter the number : "))
for a in range(1,11):
    list = [a*i for i in range(1,11)]
    print(list)
    with open("tables.txt" , "a") as f:
        f.write(str(list))
        f.write("\n")
    a =+1
