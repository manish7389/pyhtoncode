mydic = {"fan" : "fankha",
         "leptop" : "computer",
         "mobile" : "phone",
         "window" : "khidki"}
print(mydic.keys())
a=input("enter your choice : ")
# print("word minning is :" , mydic[a])
print("word minning is :" , mydic.get(a))