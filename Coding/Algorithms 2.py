loopLimit = int(input("Sequences: "))
n = 2
num1 = int(0)
num2 = int(1)
num3 = num1 + num2

print(num1)
print(num2)
print(num3)

while n < loopLimit:
    num1 = num2
    num2 = num3
    num3 = num1 + num2
    print(num3)
    n = n + 1
