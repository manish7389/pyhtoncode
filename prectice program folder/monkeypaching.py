class Test:
    def func(self):
        print("monkey patching")

        
def fun1():
    print("fun1 HE")
obj = Test()
obj.func = fun1
obj.func()