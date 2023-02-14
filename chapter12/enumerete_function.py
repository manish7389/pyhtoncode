list = [4, 7, 6, "manish", False]
# this code use for print item and index same time 
# index = 0
# for item in list:
#     print(item ,index)
#     index =+ 1
# but we can use the function for this 
for index ,item in enumerate(list):
        print(index,item)