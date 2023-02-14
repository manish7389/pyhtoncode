name = input("enter your name : ")
date = input("enter date when you want to send it : ")
# letter = (f'''hello sir,
# my name is {name},
# and i am from the student of your school
# today i have not able to come to school 
# so kindly grand me 1 day leave.
# thanks you sir!
# date : {date} ''')
letter = ('''hello sir,
my name is <|name|>,
and i am from the student of your school
today i have not able to come to school 
so kindly grand me 1 day leave.
thanks you sir!
date : <|date|> ''')
letter = letter.replace("<|name|>" , name)
letter = letter.replace("<|date|>" , date)
print(letter)