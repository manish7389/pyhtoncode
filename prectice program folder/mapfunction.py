# list = [1,2,3,4,5]
# list1 = []
# for i in list[::-1]:
#     list1.append(i)
# print(list1)


# num = [1,2,4,5,6,7]
# map_list = list(map(lambda x,y:x+y , num))
# print(map_list)




# list = [1,2,3,"c","d","+"]
# count = 0 
# for i in list:
#     if i == "c":
#         count = count - list[-4]
#     elif i == "d":
#         count = count + (list[-5]+list[-5])
#     elif i == "+":
#         count = count + list[-4]+list[-5]
#     else:
#         count = count+i

# print(count)


list = [1,2,3,"c","d","+"]
count = 0 
for i in list:
    if i == "c":
        count = count - list[2]
    elif i == "d":
        count = count + (list[1]+list[1])
    elif i == "+":
        count = count + list[1]+list[2]
    else:
        count = count+i

print(count)