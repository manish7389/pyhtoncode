list1 = [1, 2, 3, 5, 65, 57, 36, 34, 6, 567, 8, 7]
# list2 = []
# for item in list1:
#     if item%2==0:
#        list2.append(item)
# print(list2)
# *****************************/////////////*********************************
# if we want to parform some expriment on list and create a new 
# list so we can use it function to crreate a new list
list2 = [item for item in list1 if item%2==0]
print(list2)