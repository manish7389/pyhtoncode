try:
    i = int(input("enter the number : "))
    c = 1/i

except Exception as e:
    print(e)
    exit()
finally: #finally hmesha run hoga chahe apne program ko exit kr diya he fir bhi 
    print("we are secessful")

print("thanks for useing this code !")