from math import prod

n = []
products = []
full = 7316717653133062491922511

for x in str(full):
    n.append(int(x))

for i in range(0,13):
    products.append(prod(n[i:i+13]))

print(products)