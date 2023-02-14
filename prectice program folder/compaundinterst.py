p = 10000
r = 10
t = 2

amount = p*(pow((1+r/100),t))
ci = amount-p
print(ci)