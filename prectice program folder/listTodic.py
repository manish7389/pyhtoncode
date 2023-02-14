list = ["1","manish","2","kumar","3","yadav","4","patel","5","ahir"]
# new_dic = dict()
# num = 1
# for item in list:
#     if num%2 != 0:
#         new_dic[item] = list[num]
#     num = num+1

# print(new_dic)

# ************************************************///////////2WAY//////////*******************************
# print({list[i] : list[i+1] for i in range(0,len(list),2)})


# ************************************************///////////3WAY//////////*******************************
dict = dict()
for i in range(0,len(list),2):
    new_dic = {list[i]:list[i+1]}
    dict.update(new_dic)
print(dict)