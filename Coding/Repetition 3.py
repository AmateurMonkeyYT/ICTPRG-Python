while True:
    n = int(input("Enter a number: "))
    if (n < 50 or n > 70):
        print("Not within range.")
        continue
    elif (n >= 50 or n <= 70):
        print("Within range.")
        break
