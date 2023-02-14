myset = {"manish","apple","banana","khaju",8}
print(type(myset) )
print(myset)
print(len(myset))
# myset.remove("khaju")
# a  = myset.pop() this mathod is remove one iteam in set
a = myset.union({8,11}) #this funsion add a set in available se t and return a value of in one set
b = myset.intersection({8,11}) #this method get return a value of available in both set 
print(b)
print(a)
print(myset)
c = myset.add((7,8,8,9))
print(myset)