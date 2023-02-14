
from re import S


def palindrome(s):
    temp = s[::-1]
    if s == temp:
        print("Yes !! It's palindrome")
    else:
        print("No!! It's not polindrome")

s = "nitin"
palindrome(s)

#palindrome number
def palindrome2(n):
    s = str(n)
    temp = s[::-1]
    if s == temp:
        print("Yes !! It's palindrome")
    else:
        print("No!! It's not polindrome")

n = 12345654321
palindrome2(n)