def decorater_func1(func):
    def wrapper_func():
        print("hello i am wrapper func")
        return func()
    print("hello i am decrater_func1")
    return wrapper_func()

def show():
    print("hello i iam show")

decorater_show = decorater_func1(show)
# decorater_show()
