# l = [10,10,20,20,40,50,70,60,10,80,90,60,80,90,70]
# l1 = []
# for i in l:
#     if i not in l1:
#          l1.append(i)
        
# print(l1)

l = [10,10,20,20,40,50,70,60,10,80,90,60,80,90,70]
l1 = set(l)
l2 = list(l1)
l2.sort()
print(l1)
print(l2)

l = [10,10,20,20,40,50,70,60,80,90,60,80,90,70]
l1 = []
for i in l:
    if i not in l1:
         l1.append(i)
    else:
        l1.remove(i)
        
print(l1)


    
