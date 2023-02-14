def fibonnaci(n):
    if n<=1:
        return n
    else:
        return (fibonnaci(n-1) + fibonnaci(n-2))

n = 10 
if n<=0:
    print("Invalid")
else:
    for i in range(n):
        print(fibonnaci(i))