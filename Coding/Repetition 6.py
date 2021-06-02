size = int(input("Enter grid size: "))
n = 0
i = 0
while (i < size):
    while (n < size):
        print("x", end="")
        n = n + 1
    print("")
    n = 0
    i = i + 1