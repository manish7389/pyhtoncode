words = ["donkey", "mote", "kaddu","suvar"]
with open("poem.txt",) as f:
    text= f.read()


for word in words:
    data= text.replace(word, "%#$##%##")
    with open("poem.txt","w") as f:
        f.write(data)

print(data)
