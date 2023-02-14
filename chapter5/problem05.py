s  = {72,82}
print(s)
s.add(20)
s.add(20.0) # set does not store .0 value in set because is 20 and 20.0 is same value 
s.add("20")
print(s)
print(len(s))