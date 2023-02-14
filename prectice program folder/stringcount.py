str1 = "aaaabbbbcccddeeeyy"
n = len(str1)
count = 1
new_str = " "
for i in range(n-1):
    if str1[i] == str1[i+1]:
        count = count+1
    else:
        new_str = new_str + str1[i] +  str(count)
        count = 1
new_str = new_str + str1[n-1] + str(count)
print(new_str)