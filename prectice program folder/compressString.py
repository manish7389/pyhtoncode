s = "aaabbcccddddee"
count = 1
new_str = ""
n = len(s)
for i in range(n-1):
    if s[i] == s[i+1]:
        count+=1
    else:
        new_str = new_str + s[i] + str(count)
        count = 1
new_str = new_str + s[i] + str(count)
print(new_str)
