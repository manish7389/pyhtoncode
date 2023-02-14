def increment(num):
    try:
        return int(num) + 2

    except:
        raise ValueError("this is not good manish")

a = increment("50")
print(a)