from filecmp import cmp
import random

def gamewin(comp, you):
    if comp == you:
        return None
    if comp == "s":
        if you == "g":
            return True
        elif you == "w":
            return False
    elif comp == "g" :
        if you == "w":
            return True 
        elif you == "s":
            return False 
    elif comp == "w":
        if you == "s":
            return True
        elif you == "g":
            return False


randnum = random.randint(1,3)
print(randnum)
if randnum == 1:
    comp ="s"
elif randnum==2:
    comp= "g"
elif randnum==3:
    comp = "w"

you = input("player's turn snak(s) gan(g) water(w) : ")

a = gamewin(comp, you)

if a== None:
    print("this game is tie !")
elif a:
    print("you win !")
else:
    print("you lose !")
