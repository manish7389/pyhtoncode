def gretter_than(num):
    if num > 5 and num < 10:
        return True
    else:
        return False

l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# this filter funcion can filter any list like that
print(list(filter(gretter_than,l)))