import random

n = random.randint(1,10)

guess = int(input("Guess a number between 1 and 10: "))

if (guess > 10) or (guess < 1):
    print("Guess not in range")
elif (guess == n):
    print("Congratulations! You guessed correctly!")
elif (guess < n):
    print("Unlucky, you were off by", n - guess)
elif (guess > n):
    print("Unlucky, you were off by", guess - n)
print("The number was", n)