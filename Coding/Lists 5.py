numList = []

while True:
    i = input("Enter a number: ")
    if (i == "x"):
        print(numList)
        exit()
    else:
        numList.append(i)
        continue