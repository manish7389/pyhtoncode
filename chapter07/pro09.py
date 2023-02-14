n = 3
for i in range(n):
    for j in range(n):
        if ((i==0 or i==2) and (j==0 or j<=3)) or ((i==1 and j==0)):
            print(" * ",end=" ")
        else:
             print(" ",end=" ")
    print()
    # (i==0 and j<=3) or 
    # or (i==2 and j<=3)
    # ((j==0 or j==3) and i!=1)
    # ((i==0 or i==2) and (j>0 and j<2))
    # ((i==0 or i==2) and (j==0 or j<=3)) or