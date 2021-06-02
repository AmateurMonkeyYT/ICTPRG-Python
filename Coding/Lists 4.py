name = input("Enter your full name: ").upper()
name = name.split(" ")
for x in name:
    print(x[0], end="")