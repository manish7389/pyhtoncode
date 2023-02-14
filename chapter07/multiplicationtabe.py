from msilib.schema import tables


table = int(input("enter your number : "))
for i in range (1,11):
    # print(str(table)+"X"+str(i)+" = "+str(i*table))
    print(f"{i}X{table} = {i*table}")