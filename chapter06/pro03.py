text = input("enter your massage : ")
# spam = False 
if("make lot of money" in text):
         spam = True
elif("buy now" in text):
         spam = True
elif("click hare" in text):
         spam = True
elif("subscrib now" in text):
         spam = True
else:
    spam = False
if(spam):
    print("it is a spam massage please be safe !")
else:
    print("it is safe massage injoy youre day !")