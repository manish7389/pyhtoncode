def max(num1, num2, num3):
    if (num1>num2):
        if (num1>num3):
            return num1
        else:
            return num3
    else: 
        if num2>num3:
            return num2
        else:
            return num3

m = max(94,56,76)
print(str(m))


