print("Enter some numbers (press \"x\" to stop)")
total = 0
while True:
    n = input()
    if (n == "x"):
        print(total)
        break
    else:
        total = total + int(n)