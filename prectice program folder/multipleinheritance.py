class A:
    def abc(self):
        print("A")
class B(A):
    def abc(self):
        print("B")

class C(A):
    def abc(self):
        print("C")
class D(B,C):
    pass

b = D()
b.abc()

