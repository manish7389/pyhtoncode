n = 153
order = len(str(n))
sum = 0
copy_n = n
while (n>sum):
    digit = n%10
    sum += digit**order
    n = n//10

    if (sum == copy_n):
        print("it is a armstrong number")
    else:
        print("it is not a armstrong number")
print(sum)