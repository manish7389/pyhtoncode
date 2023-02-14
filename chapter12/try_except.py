while(True):
    print("press 'q' to quit the game")
    a = input("enter the number : ")
    if a == "q":
        break
    try:
        a = int(a)
        if a > 5:
            print("you are enter gretter than 5 :")
    except Exception as e:
        print(e)
print("tanks for playing game")