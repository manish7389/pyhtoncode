def splitstring(string ,word):
    newstr = string.replace(word,"manish")
    return newstr.strip()


this = "    herry hello how are you    "
n = splitstring(this , "herry")
print(n)