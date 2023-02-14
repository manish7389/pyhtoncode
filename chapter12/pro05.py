a = int(input("enter the number : "))
list = [a*i for i in range(1,11)]
print(list)
with open("table.txt" , "a") as f:
    f.write(str(list))
    f.write("\n")
