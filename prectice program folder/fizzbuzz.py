# num = 20
# if num%15 == 0:
#     print(num, "this number is FIZZBUZZ")
# elif num%3 == 0:
#     print(num, "this number is FIZZ")
# elif num%5 == 0:
#     print(num, "this number is BUZZ")
# else:
#     print("this number is not define FIZZBUZZ approch")

# ******************************++++++++++++++++++++++++***********************************

num = 20 
for i in range(1,num+1):
    if i%15 == 0:
        print("FIZZBUZZ")
    elif i%3 == 0:
        print("FIZZ")
    elif i%5 == 0:
        print("BUZZ")
    else:
        print(i)