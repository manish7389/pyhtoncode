try:
    a = int(input("enter a number : "))
    b = 1/a
    print(b)

except Exception as e:
    print("error accured :1")

except ZeroDivisionError as e:
    print("error accured 2")
    print(e)