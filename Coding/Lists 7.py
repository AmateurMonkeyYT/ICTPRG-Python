numList = []
dupeList = []

while True:
    i = input("Enter a number: ")
    if (i == "x"):
        print(dupeList)
        exit()
    elif (i in numList) and (i not in dupeList):
            dupeList.append(i)
            continue
    else:
        numList.append(i)