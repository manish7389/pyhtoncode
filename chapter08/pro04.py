def summ(num):
    if num==0 or num ==1:
        return 
    else:
        return num + summ(num-1)
s = summ(5)
print(str(s))