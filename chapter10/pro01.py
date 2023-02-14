class Programmer():
    company = "microsoft"
    def __init__(self, name , product):
        self.name = name
        self.product = product
    def detail(self):
        print(f"the programmer name is {self.name} and work on produt {self.product} and company is {Programmer.company}")

manish = Programmer("manish", "github")
herry = Programmer("herry", "skype")
manish.detail()
herry.detail()