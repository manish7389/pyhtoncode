name = input("enter your name : ")
date = input("enter the date : ")
print("good morning " + name)
letter ='''dear |<name>|
    you are selected for the second round of interview,
    please come tommoro for second round 
    best of luck! 
    thanks you!
    date = |<date>| 
'''
letter = letter.replace("|<name>|" , name)
letter = letter.replace("|<date>|" , date)
print(letter)
