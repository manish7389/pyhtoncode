# s = "nitin"
def palindrome(s):
    temp = s[::-1]
    if s == temp:
        print("it is a palindrome string")

    else:
        print("it is not a palindrome string")

s = palindrome("manish")
# *****************************************************************************************
def palindromenumber(num):
    num = str(num)
    temp = num[::-1]
    if num == temp:
        print("it is a palindrome number")

    else:
        print("it is not a palindrome number")

num = palindromenumber(191)