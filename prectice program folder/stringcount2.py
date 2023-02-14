s = "aaaabbbcccddddeeeesssff"
n = len(s)
list = []
str = " "
count = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        count = count+1
    else:
        list.append(count)
        str = str+s[i]
        count = 1
list.append(count)
str = str+s[n-1]
print(list)
print(str)


st = "a8b6c2d5h1"
max = 0
min = st[1]
minm = int(min)
for i in st[1::2]:
    c = i
    d = int(c)
    if d > max:
        max = d
    elif d < minm:
        min = d

print(max)
print(min)
