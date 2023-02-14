# 0 1 1 3 5 8 13 21 34 55 89 144
list = []
def fibonachi(n):
    num1 = 0 
    num2 = 1
    list.append(num1)
    while num2<n:
        list.append(num2)
        num3 = num1+num2
        num1 = num2
        num2 = num3

fibonachi(150)
print(list)

