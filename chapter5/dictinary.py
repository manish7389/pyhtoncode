mydic ={
    "name" : "manish",
    "from" : "indore",
    "mnu" : "7389021175",
    "mark" : "[78,89,69]",
}
a = mydic["name"]
print(a)
print(mydic["mark"])
b = mydic.items()
print(b)
print(mydic.keys())
mydic.update({"friend" : "harry"})
print(mydic)
print(mydic.get("name"))
