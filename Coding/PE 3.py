x = int(input("Enter a number to factorise: "))
n = 2
a = 1
b = 2

while (n < x):

    if (x % n != 0):
        n += 1
        continue

    elif (x % n == 0):
        a = x / n
        print("Testing", a)

        while True:

            if (a == b):
                print(a, "is the largest prime factor.")
                exit()

            elif (a % b == 0):
                print (a, "was a factor, but was not prime.")
                b = 2
                n += 1
                break

            elif (a % b != 0):
                b += 1
                continue

print(x, "has no prime factors")