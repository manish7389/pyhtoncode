d = {}
i = 0
while i<4 :
      name = input("enter the name : ")
      lang = input("enter your fav language : ")
      d.update({name : lang})
      i=i+1
print(d)
# problem07 if we give you same name and anather language so last language are show in dic
# proble08 we can do sane language for two name same lauguage 
# proble09 can we change the list in side the set 
# so it will return rerror becauge we can not save in list in side of set 
# but we can save tuple in side the set but also we can not change it   