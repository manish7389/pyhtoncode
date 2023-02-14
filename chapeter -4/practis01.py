mydic  = {
    "fankha" : "fan",
    "khach" : "glass",
    "computer" : "leptop",
    "phone" : "mobile",
}
print("select the word you want to khow  : " , mydic.keys())
a = input("enter the word  : ")
# print(mydic[a])
print(mydic.get(a)) #if do you not want to show error so you can use this methods 