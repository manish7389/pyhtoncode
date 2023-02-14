# f = open("poem.txt", "w")
# text = f.write("twinkle twinkle little star how are wonder what you are !")
# f.close()
f = open("poem.txt", "r")
text = f.read()
if "twinkle" in text:
    print("twinkle is prsent in this poem")
else:
    print("twinkle is not prsent in this poem")
f.close()