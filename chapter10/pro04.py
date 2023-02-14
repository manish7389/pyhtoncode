class Calculater():
    def __init__(self, number):
        self.number = number
    def squre(self):
        print(f"the squre of the number is {self.number**2}")
    def squreroot(self):
        print(f"the squre of the number is {self.number**0.5}")
    def quebe(self):
        print(f"the squre of the number is {self.number**3}")
    @staticmethod
    def greet():
        print("********hello welcome to best calculater in the word******")
a = Calculater(5)
a.greet()
a.squre()
a.squreroot()
a.quebe()