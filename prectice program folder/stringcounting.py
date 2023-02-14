s = "aaaabbbcccddddiiisssff"
n = len(s)
dic = {}
count = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        count = count+1

    else:
        dic.update({s[i]:str(count)})
        count = 1
dic.update({s[n-1]:str(count)})
print(dic)
result = min(dic,key=dic.get)
print(result)
print(dic.get(result))
