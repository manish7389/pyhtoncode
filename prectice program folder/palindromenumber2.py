
def pelindrome(num):
    n = len(num)
    for i in range(n):
        if num[i] != num[n-i-1]:
            return False

    return True

number = pelindrome("54245")
print(number)


def palindrome2(num):
    reverse_num = reversed(num)
    # for i in reverse_num:
    temp = ''.join(reverse_num)
    if num == temp:
        return True
    else:
        return False
str = palindrome2("manish")
print(str)