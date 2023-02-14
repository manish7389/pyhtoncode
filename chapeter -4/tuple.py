# t = () empty tuple
# t = (1,) itis one element of tuple
t  = ( 1,3,4,9,3,35,2,34) # multiple element of tuple 
print(t.count(3))
print(t.index(9))
print(t.__add__((5,5,7))) # add method addd two tuple to in a single tuple 
print(t)
# t[0] = 45 'tuple' object does not support item assignment
# t.append(45) it is give you a error
tuple = (0,0,76,64,63,0,6,0)
print(tuple.count(0))