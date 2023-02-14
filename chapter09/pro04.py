with open("poem.txt",) as f:
    text= f.read()
if "twinkle" in text:
    data= text.replace("twinkle", "%#$##%##")
print(data)
with open("poem.txt","w") as f:
    text= f.write(data)